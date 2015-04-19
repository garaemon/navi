# navi.core.log
from logging import getLogger,StreamHandler,DEBUG, Formatter

class LoggingObject:
    def __init__(self):
        self.logger = getLogger(__name__)
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(handler)
