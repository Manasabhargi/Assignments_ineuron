import logging
logging.basicConfig(filename = "test10.log", level = logging.DEBUG, format = "%(message)s")
import random
try:
    s = random.choice('Sudhanshu')
    logging.info(s)
except Exception as e:
    logging.exception(e)