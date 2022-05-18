import logging
from bubblecam_config import * # Cam config constants
import time
import os
import datetime
from queue import Queue
import threading
lock = threading.Lock()

class Logger():
    
    def __init__(self, isCam: bool, cam_log_write: bool = False):
        if isCam:
            LOG_MODE = 'write' if cam_log_write else 'capture'

        currDate = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
        LOG_FILENAME = f'./logs/{currDate}_{LOG_FILE}_{LOG_MODE}.log'
        open(LOG_FILENAME, 'w')
        
        # Create logger
        logging.basicConfig(
			filename=LOG_FILENAME,
			filemode=FILEMODE,
			format=MESSAGE_FORMAT,
			datefmt=DATE_FORMAT,
			level=logging.DEBUG,
    	)

        self.logger = logging.getLogger()
        self.logger.debug(f"Logger created for {__file__}.")

    
    

# logger = Logger(True, "bcam", "info", "test.log", "bubblecam logs")
# logger.log_data("Captured image")