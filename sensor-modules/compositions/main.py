from bubblecam import BubbleCam
from logger import Logger
from ..state import State
from queue import Queue
from bubblecam_config import *


if __name__ == '__main__':
	curr_state = State.QUIESCENT
	# Event loop 
	while True:
		if curr_state == State.STORM:
			# Create two logger instances 
			loop_logger = Logger(True, False) # Logger for image capture loop
			write_logger =  Logger (True, True) # Logger for write loop

			# BubbleCam instance
			bubblecam = BubbleCam(loop_logger)

			# Create a queue for the shared data
			queue = Queue(ROLL_BUF_SIZE)

			# Launch two threads for the capture 

			# Receive wavebreak signal





			
