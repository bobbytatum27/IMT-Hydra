from collections import deque
import cv2
import datetime
import time
import sys
import os
from .logger import Logger
from queue import Queue
from .cam_comp import Cam
from .state import State # Glider States
import threading

from bubblecam_config import * # Cam config constants

class BubbleCam():

	def __init__(self, clogger: Logger, wlogger: Logger):
		# Capture and write logger (writes to separate files)
		self.clogger = clogger.logger
		self.wlogger = wlogger.logger
		self.cam = Cam('bubblecam', self.capture_function, EXPOSURE, GAIN, BRIGHTNESS, GAMMA, FPS, BACKLIGHT, 0, IMG_TYPE, ROLL_BUF_SIZE)
		self.glider_state = State.QUIESCENT


	def capture_function(self, buffer: deque, lock): # not sure if local reference for buffer is okay but will see in test
		"""
		Continuously log data in a shared queue.
		"""
		while True:
			# time.sleep(0.1)
			try:	
				if self.glider_state.value == State.STORM:
					# in Storm state read frame, encode image, append to rolling buffer
					# TODO(pkam): check success & result values since these ops can fail
					success, frame = self.cam.capture_image()
					result, img = cv2.imencode(IMG_TYPE, frame)

					with lock:
						# if buffer is full, remove the earliest image and add the latest image
						if not len(buffer) < self.cam.buffer_size:
							buffer.popleft()
						buffer.append(img) 
						self.clogger.info("Captured image")
			except:
				self.clogger.error("Exception occurred", exc_info=True)


	def write_images(self, buffer: deque, lock):
		"""
		Write images from buffer into memory
		"""

		def getDateTimeIso():
				"""
				Returns the current date and time in ISO format 
				"""
				return datetime.datetime.now().isoformat()

		# Create a new directory for this event
		dtime_str = getDateTimeIso()
		dtime_path = os.path.join(IMG_DIR, dtime_str)
		os.mkdir(dtime_path)
		start_time = time.time() # time the write speed
		num_captured = 0 # number images in order

		time.sleep(EVENT_DELAY) # scrappy solution to "look forward"
		
		with lock:
			try:
				num_captured = 0 # number images in order
				start_time = time() # time the write speed

				# reverse rolling buffer to get last image captured first and write to disk
				for img in list(reversed(buffer)):
					# data validation 
					if sys.getsizeof(img) < BYTE_THRESHOLD:
						continue
					img_str = f"img_{num_captured}" + IMG_TYPE
					img.tofile(os.path.join(dtime_path, img_str)) 
					num_captured += 1

				write_speed = time() - start_time
				self.wlogger.debug(f"Wrote {num_captured} images to disk at {dtime_path} in {write_speed} seconds.")
				return num_captured, write_speed
			except:
				self.wlogger.error("Exception occurred", exc_info=True)
				return 0, None
			finally:
				time.sleep(LOCKOUT_DELAY)

	def capture_image(self):
		return self.cam.capture_image()

	def start_workflow(self):
		self.cam.start_workflow()
		self.glider_state = State.STORM
		self.clogger.info("Started workflow")
		self.wlogger.info("Started workflow")
		return True
	
	def power_off(self):
		self.cam.power_off()
