import logging
logging.basicConfig(filename = "test3.log", level = logging.DEBUG,  format = "%(message)s")
import math
try:
    math.sqrt(100)
    logging.info(math.sqrt(100))
except Exception as e:
    logging.exception(e)
