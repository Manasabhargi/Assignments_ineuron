import logging
logging.basicConfig(filename = "test.log", level = logging.DEBUG, format = '%(message)s')

try:
    def __init__(self):
        logging.info("To illustrate python package")
except Exception as e:
    logging.exception(e)