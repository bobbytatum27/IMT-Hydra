import cv2
import time
from .logger import Logger
from queue import Queue
from .cam_comp import Cam
from ..state import State # Glider States
import threading
lock = threading.Lock()

from bubblecam_config import * # Cam config constants

class BubbleCam():

	def __init__(self, logger: Logger):
		self.logger = logger
		self.cam = Cam('bubblecam', capture_function, EXPOSURE, GAIN, BRIGHTNESS, GAMMA, FPS, BACKLIGHT, 0, IMG_TYPE, ROLL_BUF_SIZE)
		self.glider_state = State.STORM


	def capture_function(self, queue: Queue):
		"""
		Continuously log data in a shared queue.
		"""
		while True:
			time.sleep(0.1)
			try:	
				if self.glider_state.value == State.STORM:
					# in Storm state read frame, encode image, append to rolling buffer
					# TODO(pkam): check success & result values since these ops can fail
					success, frame = self.camera.read()
					result, img = cv2.imencode(IMG_TYPE, frame)
					queue.append(img) 
					self.logger.info("Captured image")
			except:
				self.logger.error("Exception occurred", exc_info=True)
	
	def power_off(self):
		self.cam.power_off()
