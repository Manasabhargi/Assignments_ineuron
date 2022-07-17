import logging

logging.basicConfig(filename = "test9.log", level = logging.DEBUG,  format = "%(message)s")
import collections

try:
    d1 = collections.OrderedDict()
    logging.info("d1['A'] = 65")
    logging.info("d1['C'] = 67")
    logging.info("d1['B'] = 66")
    logging.info("d1['D'] = 68")

    for k, v in d1.items():
        print(k, v)
except Exception as e:
    logging.exception(e)