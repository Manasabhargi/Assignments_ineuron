import logging
logging.basicConfig(filename = "test7.log", level = logging.DEBUG,  format = "%(message)s")
import statistics
try:
    logging.info(statistics.mean([2,5,6,9]))
except Exception as e:
    logging.exception(e)