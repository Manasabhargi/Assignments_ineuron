import logging
logging.basicConfig(filename = "test6.log", level = logging.DEBUG,  format = "%(message)s")
import sys
try:
    logging.info(sys.maxsize)
except Exception as e:
    logging.exception(e)