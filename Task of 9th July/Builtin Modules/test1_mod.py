import logging
logging.basicConfig(filename = "test1.log", level = logging.DEBUG,  format = "%(message)s")
import platform
try:
    x = platform.system()
    logging.info(x)
except Exception as e:
    logging.exception(e)