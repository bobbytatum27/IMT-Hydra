from .cam import Cam
from .state import State # Enums: {Quiescent, Storm, Event}

# Copied from cSBC (Will remove unused modules as necessary)
import os
import cv2
# import logging
import EasyPySpin
import multiprocessing as mp
from collections import deque

# import constants for this file
from config.bubblecam_config import *


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
				camera: EasyPySpin.VideoCapture, 
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
		super().__init__(camera, exposure, gain, brightness, fps, backlight, 
						current_state, event_delay, image_type, buffer_size, buffer)
		# If we do this might not need current_state?
		


	# Methods inherited from Sensor via Cam

	def power_on(self):
		"""
		Creates a camera reference and stores it in the appropriate member variable
		"""
		super()

		 # set the camera settings
		self.camera.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE)
		self.camera.set(cv2.CAP_PROP_GAIN, GAIN)
		self.camera.set(cv2.CAP_PROP_BRIGHTNESS, BRIGHTNESS)
		self.camera.set(cv2.CAP_PROP_GAMMA, GAMMA)
		self.camera.set(cv2.CAP_PROP_FPS, FPS)
		self.camera.set(cv2.CAP_PROP_BACKLIGHT, BACKLIGHT)

	def power_off(self):
		"""
		A call to the camera reference's release() method
		"""
		super()
	
	def write_data(self, file_handler):
		"""
		Write the data in the buffer to file
		"""
		try:
			# number images in order
			num_captured = 0
			# create new dir to store images for this event
			# dtime_path = createDatetimePath()

			# reverse rolling buffer to get last image captured first and write to disk
			for img in list(reversed(self.buffer)):
				img_str = f"img_{num_captured}" + IMG_TYPE
				img.tofile(os.path.join("Test Datetime", img_str))
				# increment counters and log write
				file_handler.value += 1
				num_captured += 1

			return num_captured
		except:
			# logger.error("Exception occurred", exc_info=True)
			print("exception occurred")

	def collect_data(self):
		"""
		Continuously log data in a double-ended queue.
		"""
		try:
			while True:
				# in standby read frame, encode image, append to rolling buffer
				success, frame = self.camera.read()
				result, img = cv2.imencode(IMG_TYPE, frame)
				self.buffer.append(img)
		except:
			# logger.error("Exception occurred", exc_info=True)
			print("exception occurred")
		# release the camera and exit
		finally:
			self.camera.release()
			# logger.info("Successfully released camera.")
			print("camera released")
		
	# Bubblecam member methods inherited from Cam

	def set_state(self, next_state: State):
		"""
		Changes the state of the cam to the passed parameter
		"""
		super(State)
	
	def detect_event(self):
		"""
		Triggers the Bubble Cam event response -> collects data and logs event time
		"""
		...
		self.write_data() # pass some file handler in here
		# log time
