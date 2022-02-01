# Python Standard Library Modules
import os
import logging
import datetime
import multiprocessing as mp
from collections import deque

# Copied from cSBC (Will remove unused modules as necessary)
# Third Party Modules
import cv2
import EasyPySpin

# Local Modules
from config.bubblecam_config import * # Cam config constants
from .cam import Cam
from .state import State # Enums: {Quiescent, Storm, Event}

class BubbleCam(Cam):
	"""
    Bubble cam class which inherits from Cam
	
    Attributes
    ----------
    
    camera : EasyPySpin.VideoCapture
    exposure : int
    gain : int
    brightness : int
    gamma : float
    fps : int
    backlight : int
    current_state : Enum {Quiescent, Storm, Event}
    event_delay : int
    image_type : String
    buffer_size : int
    buffer : Deque

    Methods
    -------
    
    power_on()
        creates a camera reference and stores it in the appropriate member variable
    power_off()
        a call to the camera reference's release() method; see cSBC.py
    write_data(file_handler?)
        write the data in the buffer to file
    collect_data()
        continuously log data in a double-ended queue.
    set_state(next_state: Enum {Quiescent, Storm, Event})
        changes the state of the cam to the passed parameter
    detect_event()
        triggers the Bubble Cam event response -> collects data and logs event time
    """

	# Initialize Member Variables
	def __init__(self,  
				exposure: int, 
				gain: int, 
				brightness: int, 
				fps: int, 
				backlight: int, 
				current_state: State,
				event_delay: int,
				image_type: str,
				buffer_size: int, 
				buffer: deque):
		super().__init__(exposure, gain, brightness, fps, backlight, 
						current_state, event_delay, image_type, buffer_size, buffer)

		# Create logger
		logging.basicConfig(
			filename=LOG_FILE,
			filemode=FILEMODE,
			format=MESSAGE_FORMAT,
			datefmt=DATE_FORMAT,
			level=logging.DEBUG,
    	)

		logger = logging.getLogger()
		logger.debug(f"Logger created for {__file__}.")
		
		# Create a shared variable to track state across processes
		self.shared_state = mp.Value("i", current_state)

		# Start another process to run collect_data() in the background 
		p1 = mp.Process(
            target=self.collect_data,
            args=(self.shared_state),
        )

		p1.start()

		# The process will run until the instance of BubbleCam is deleted and p1.join() will automatically run
		# A potential fix to this would be to check current_state at initialization and during set_state()
		# and only start the process when appropriate (Storm, Event).
		
	# Methods inherited from Sensor via Cam
	def power_on(self):
		"""
		Creates a camera reference and stores it in the appropriate member variable
		"""
		super().power_on()

		 # set the camera settings
		 # TODO(punnkam): check if these should be values received in ctor
		self.camera.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE)
		self.camera.set(cv2.CAP_PROP_GAIN, GAIN)
		self.camera.set(cv2.CAP_PROP_BRIGHTNESS, BRIGHTNESS)
		self.camera.set(cv2.CAP_PROP_GAMMA, GAMMA)
		self.camera.set(cv2.CAP_PROP_FPS, FPS)
		self.camera.set(cv2.CAP_PROP_BACKLIGHT, BACKLIGHT)
	
	def write_data(self, file_handler):
		"""
		Write the data in the buffer to file
		"""

		# Create a new directory for this event
		dtime_str = self.getDateTimeIso()
		dtime_path = os.path.join(IMG_DIR, dtime_str)
		os.mkdir(dtime_path)

		try:
			# number images in order
			num_captured = 0

			# reverse rolling buffer to get last image captured first and write to disk
			for img in list(reversed(self.buffer)):
				img_str = f"img_{num_captured}" + IMG_TYPE
				img.tofile(os.path.join(dtime_path, img_str)) 

				# increment counters and log write
				num_captured += 1

			self.logger.debug(f"Wrote {num_captured} images to disk at {dtime_path}.")
			return num_captured
		except:
			self.logger.error("Exception occurred", exc_info=True)

	def collect_data(self, shared_state):
		"""
		Continuously log data in a double-ended queue.
		"""
		try:	
			while True:
				if shared_state.value == State.Storm:
					# in Storm state read frame, encode image, append to rolling buffer
					success, frame = self.camera.read()
					result, img = cv2.imencode(IMG_TYPE, frame)
					self.buffer.append(img)
				elif shared_state.value == State.WAVEBREAK:
					# in Wavebreak Event state, call write_data() to store data on disk
					if self.buffer:
						self.logger.debug(f"Writing images to disk.")
						self.write_data() # pass in some file_handler  
						self.buffer.clear
						self.logger.debug(f"Clear buffer.")
					else:
						self.logger.debug(f"Buffer empty. Did nothing.")

					# change state to Storm
					with self.shared_state.get_lock():
						self.shared_state.val = State.Storm
		except:
			self.logger.error("Exception occurred", exc_info=True)
		# release the camera and exit
		finally:
			self.camera.release()
			self.logger.info("Successfully released camera.")
	
	def detect_event(self):
		"""
		Triggers the Bubble Cam event response -> collects data and logs event time
		"""
		# set current_state to event 
		self.set_state(State.WAVEBREAK)

		# set shared_state to event (must get lock first)
		with self.shared_state.get_lock():
			self.shared_state.val = State.WAVEBREAK

		self.logger.info(f"Event triggered at {self.getDateTimeIso()}")

	# Misc Helpers
	def getDateTimeIso():
		return datetime.datetime.now().isoformat()