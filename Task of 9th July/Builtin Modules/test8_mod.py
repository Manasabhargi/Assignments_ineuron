import logging
import time
logging.basicConfig(filename = "test8.log", level = logging.DEBUG,  format = "%(message)s")
try:
   logging.info(time.time())
except Exception as e:
    logging.exception(e)