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
        # self.isCam = isCam
        # self.name = name
        # format_string = f'[%(asctime)s: {self.name.upper()}: %(levelname)s] : %(message)s'
        # format_date = '%Y-%m-%dT%H:%M:%S'

        # # BASIC CONFIG
        # if path is not None:
        #     logging.basicConfig(filename=path, filemode='a', format=format_string, datefmt=format_date)

        # # START LOGGER
        # self.logger = logging.getLogger(nameLog)

        # if path is None:
        #     # DEFINE FORMAT 
        #     handler = logging.StreamHandler()
        #     formatter = logging.Formatter(fmt=format_string, datefmt=format_date)
        #     handler.setFormatter(formatter)
        #     logger.addHandler(handler)

        # # LEVEL SET
        # self.logger.setLevel(logging.INFO)

        # self.logger.info('BEGIN LOGGING')
        if isCam:
            LOG_MODE = 'write' if cam_log_write else 'capture'

        LOG_FILENAME = f'logs/{LOG_FILE}_{LOG_MODE}.log'
        
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


    def consume(self, queue: Queue):
        """
        Used for consuming data from a shared variable (camera is the producer)
        """

		# Create a new directory for this event
		dtime_str = self.getDateTimeIso()
		dtime_path = os.path.join(IMG_DIR, dtime_str)
		os.mkdir(dtime_path)
        start_time = time.time() # time the write speed
        num_captured = 0 # number images in order

        while True:
            try:
                time.sleep(0.2)
                # reverse rolling buffer to get last image captured first and write to disk
                image = queue.get()
                img_str = f"img_{num_captured}" + IMG_TYPE
                img.tofile(os.path.join(dtime_path, img_str)) 
                num_captured += 1
            except queue.Empty:
                break
            else:
                self.logger.error("Exception occurred", exc_info=True)
                return 0, None

        write_speed = time.time() - start_time
        self.logger.info(f"Wrote {num_captured} images to disk at {dtime_path} in {write_speed} seconds.")
        return num_captured, write_speed
        
    def getDateTimeIso():
		return datetime.datetime.now().isoformat()

    
    

# logger = Logger(True, "bcam", "info", "test.log", "bubblecam logs")
# logger.log_data("Captured image")