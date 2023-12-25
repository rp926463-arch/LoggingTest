import logging


class NumberGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # for attribute in dir(self.logger):
        #     value = getattr(self.logger, attribute)
        #     print(f"{attribute}: {value}")

    def generate_number(self):
        self.logger.info('In generate number, info')  # running from main.py
        self.logger.debug('In generate number, debug')
        self.logger.error("Hey error occured..")

