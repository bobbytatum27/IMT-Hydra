from .cam import Cam

# Copied from cSBC (Will remove unused modules as necessary)
import os
import cv2
import time
import socket
import shutil
import logging
import datetime
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
		...

	def collect_data():
		"""
		Continuously log data in a double-ended queue.
		"""
		...
	
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
