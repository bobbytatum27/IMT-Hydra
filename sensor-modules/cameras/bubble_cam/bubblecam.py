# Python Standard Library Modules
import os
import logging
import datetime
import multiprocessing as mp
from time import time

# Copied from cSBC (Will remove unused modules as necessary)
# Third Party Modules
import cv2
import EasyPySpin # We might be able to remove this

# Local Modules
from bubblecam_config import * # Cam config constants
from ..cam import Cam
from ...state import State # Glider States

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
    event_delay : int
    image_type : String
    buffer_size : int
    buffer : Deque
	initial_state: State
	is_locked_out: Multiprocessing.Value

    Methods
    -------
    
    power_on()
        creates a camera reference and stores it in the appropriate member variable
    power_off()
        a call to the camera reference's release() method; see cSBC.py
    write_data(file_handler?)
        write the data in the buffer to file
    collect_data()
        continuously log data in a double-ended queue
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
				event_delay: int,
				image_type: str,
				buffer_size: int,
				initial_state: State):
		super().__init__(exposure, gain, brightness, fps, backlight, event_delay, 
						image_type, buffer_size, initial_state)

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

		# Another process to run collect_data() in the background 
		self.collect_data_proc = mp.Process(
            target=self.collect_data,
            args=(self.glider_state),
        )
		# For locking out the camera when an event occurs
		self.is_locked_out = mp.Value("i", False)

		
	# Methods inherited from Sensor via Cam
	def power_on(self):
		"""
		Creates a camera reference and stores it in the appropriate member variable
		"""
		super().power_on()

		# set the camera settings
		self.camera.set(cv2.CAP_PROP_EXPOSURE, self.exposure)
		self.camera.set(cv2.CAP_PROP_GAIN, self.gain)
		self.camera.set(cv2.CAP_PROP_BRIGHTNESS, self.brightness)
		self.camera.set(cv2.CAP_PROP_GAMMA, self.gain)
		self.camera.set(cv2.CAP_PROP_FPS, self.fps)
		self.camera.set(cv2.CAP_PROP_BACKLIGHT, self.backlight)

		# Start capturing images via another process
		# The process will run until the instance of BubbleCam is deleted and p1.join() will automatically run.
		# A potential fix to this would be to check current_state at initialization and during set_state()
		# and only start the process when appropriate (Storm, Event).
		self.collect_data_proc.start()
	
	def write_data(self):
		"""
		Write the data in the buffer to file
		"""

		# Create a new directory for this event
		dtime_str = self.getDateTimeIso()
		dtime_path = os.path.join(IMG_DIR, dtime_str)
		os.mkdir(dtime_path)

		try:
			num_captured = 0 # number images in order
			start_time = time() # time the write speed

			# reverse rolling buffer to get last image captured first and write to disk
			for img in list(reversed(self.buffer)):
				img_str = f"img_{num_captured}" + IMG_TYPE
				img.tofile(os.path.join(dtime_path, img_str)) 
				num_captured += 1

			write_speed = time() - start_time
			self.logger.debug(f"Wrote {num_captured} images to disk at {dtime_path} in {write_speed} seconds.")
			return num_captured, write_speed
		except:
			self.logger.error("Exception occurred", exc_info=True)
			return 0, None

	def collect_data(self):
		"""
		Continuously log data in a double-ended queue.
		"""
		try:	
			while True:
				if self.glider_state.value == State.STORM:
					# in Storm state read frame, encode image, append to rolling buffer
					# TODO(pkam): check success & result values since these ops can fail
					success, frame = self.camera.read()
					result, img = cv2.imencode(IMG_TYPE, frame)
					self.buffer.append(img)
				elif self.glider_state.value == State.WAVEBREAK:
					# in Wavebreak Event state, call write_data() to store data on disk
					if len(self.buffer) != 0:
						self.logger.debug(f"Writing images to disk.")
						self.write_data() # pass in some file_handler  
						self.buffer.clear()
						self.logger.debug(f"Clear buffer.")
					else:
						self.logger.debug(f"Buffer empty. Did not write any images to disk.")

					# Lockout camera for 60 seconds, but resume storm state.
					# TODO(pkam): Determine what to do if STORM state is NOT the right state to return to. 
					# (i.e.) Storm -> Wavebreak -> Quiescent
					# It's very unlikely that we go from Wavebreak to Quiescent, but it is something to consider. Do we care about this edge case?
					self.set_state(State.STORM)
					self.set_camera_lockout(True)
		except:
			self.logger.error("Exception occurred", exc_info=True)
		# release the camera and exit
		finally:
			self.power_off()
			self.logger.info("Successfully released camera.")
		
	def detect_event(self):
		"""
		Triggers the Bubble Cam event response -> collects data and logs event time.
		State transition only occurs when camera is not in lockout mode.
		"""
		# Only set the state if it's not lockout mode.
		# If it is in lockout mode, use the time delta to see if 1 minute has passed.
		if (bool(self.is_locked_out.value)):
			if (time() - self.time_locked_out > self.event_delay):
				self.set_camera_lockout(False)
		else:
			# set current_state to event state
			self.set_state(State.WAVEBREAK)
			self.logger.info(f"Event triggered at {self.getDateTimeIso()}")

	def set_camera_lockout(self, is_locked_out: bool):
		# set the lockout variable
		with self.is_locked_out.lock():
			self.is_locked_out.value = is_locked_out
		# if lockout mode entered, save the time at which it started for later use in computing total lockout time
		if (is_locked_out):
			self.time_locked_out = time()

	# Misc Helpers
	def getDateTimeIso():
		return datetime.datetime.now().isoformat()