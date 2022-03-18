import logging

class Logger():
    
    def __init__(self, level: str, path: str, name: str):
        format_string = '%(asctime)s : T%(relativeCreated)05ds : %(levelname)-8s - %(name)s : %(message)s'
        format_date = '%Y-%m-%dT%H:%M:%S'

        # BASIC CONFIG
        if path is not None:
            logging.basicConfig(filename=path, filemode='a', format=format_string, datefmt=format_date)

        # START LOGGER
        logger = logging.getLogger(name)

        if path is None:
            # DEFINE FORMAT 
            handler = logging.StreamHandler()
            formatter = logging.Formatter(fmt=format_string, datefmt=format_date)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        # LEVEL SET
        logger.setLevel(logging.DEBUG)

        logger.info('TEST')

        self.logger = logging.getLogger(__name__)
        self.logger.info(f'START NEW EXECUTION\n\n{"=" * 36}\n')

    def log_data():
        ...

    def write_data():
        ...