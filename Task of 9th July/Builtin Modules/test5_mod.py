import logging
logging.basicConfig(filename = "test5.log", level = logging.DEBUG,  format = "%(message)s")
import random
try:
    logging.info(random.randint(1,1000))
except Exception as e:
    logging.exception(e)