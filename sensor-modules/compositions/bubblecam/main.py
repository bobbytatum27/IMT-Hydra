from asyncore import write
from bubblecam import BubbleCam
from logger import Logger
from .state import State
from bubblecam_config import *
from collections import deque
import threading

if __name__ == '__main__':

	curr_state = State.QUIESCENT

	# Create a queue for the shared data
	queue = deque()

	# Create a lock for the queue
	lock = threading.Lock()

	#Event loop 
	# TODO: This turns on Bubblecam in all states (might not want that)
	bubblecam = BubbleCam(Logger(True, False), Logger (True, True))

	# Create two logger instances for capturing and writing
	# Launch two threads for the capture and write function
	captureThread = threading.Thread(target=bubblecam.capture_function, args=(queue, lock))
	writeThread = threading.Thread(target=bubblecam.write_images, args=(queue, lock))

	while True:
		if curr_state == State.STORM:
			# Start the capture thread
			captureThread.start()

		# Receive wavebreak signal
		# Test receive for now
		elif curr_state == State.WAVEBREAK:
			writeThread.start()
			writeThread.join()
			curr_state = State.STORM
		else:
			continue





			
