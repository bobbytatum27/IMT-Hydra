import logging

class Logger():
    
    def __init__(self, isCam: bool, cam: str, level: str, path: str, name: str):
        self.isCam = isCam
        self.cam = cam
        format_string = '%(asctime)s : %(message)s'
        format_date = '%Y-%m-%dT%H:%M:%S'

        # BASIC CONFIG
        if path is not None:
            logging.basicConfig(filename=path, filemode='a', format=format_string, datefmt=format_date)

        # START LOGGER
        self.logger = logging.getLogger(name)

        if path is None:
            # DEFINE FORMAT 
            handler = logging.StreamHandler()
            formatter = logging.Formatter(fmt=format_string, datefmt=format_date)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        # LEVEL SET
        self.logger.setLevel(logging.DEBUG)

        self.logger.info('BEGIN LOGGING')

    def log_data(self, data: str):
        if self.isCam:
            self.logger.info(f'{self.cam.upper()}: {data}\n')
    
    

# logger = Logger(True, "bcam", "info", "test.log", "bubblecam logs")
# logger.log_data("Captured image")