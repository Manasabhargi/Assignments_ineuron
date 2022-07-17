"""The dir() is used list all the function names (or variable names) in a module."""
import logging
logging.basicConfig(filename = "test2.log", level = logging.DEBUG,  format = "%(message)s")
import platform
try:
    x = dir(platform)
    logging.info(x)
except Exception as e:
    logging.exception(e)


