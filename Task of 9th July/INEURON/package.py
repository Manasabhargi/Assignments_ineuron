import logging
logging.basicConfig(filename ="pac.log", level = logging.DEBUG, format ='%(message)s')

from INEURON import *


try:
    obj1 = ds()
    obj1.course_ds()

    obj2 = ml()
    obj2.course_ml

except Exception as e:
    logging.exception(e)