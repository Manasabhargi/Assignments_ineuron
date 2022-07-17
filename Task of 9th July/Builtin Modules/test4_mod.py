import logging
logging.basicConfig(filename = "test4.log", level = logging.DEBUG,  format = "%(message)s")
import os
try:
    logging.info(os.listdir("C:\\Users"))
except Exception as e:
    logging.exception(e)
