import logging.config
import json
from utils.NumberGenerator import NumberGenerator


class Main:
    def __init__(self):
        pass

    def run(self):
        # Load logging configuration from JSON file
        with open('./config/logging_config.json', 'rt') as f:
            logging_config = json.load(f)

        logging.config.dictConfig(logging_config)

        # Get the logger using __name__
        logger = logging.getLogger(__name__)

        logger.info('Hello, info')  # running from main.py
        logger.debug('Hello, debug')

        nmb = NumberGenerator()
        nmb.generate_number()


if __name__ == '__main__':
    obj = Main()
    obj.run()
