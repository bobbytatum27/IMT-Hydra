import logging

class Logger():
    
    def __init__(self, isCam: bool, name: str, level: str, path: str, nameLog: str):
        self.isCam = isCam
        self.name = name
        format_string = f'[%(asctime)s: {self.name.upper()}: %(levelname)s] : %(message)s'
        format_date = '%Y-%m-%dT%H:%M:%S'

        # BASIC CONFIG
        if path is not None:
            logging.basicConfig(filename=path, filemode='a', format=format_string, datefmt=format_date)

        # START LOGGER
        self.logger = logging.getLogger(nameLog)

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
            self.logger.info(f'{data}\n')
    
    

# logger = Logger(True, "bcam", "info", "test.log", "bubblecam logs")
# logger.log_data("Captured image")