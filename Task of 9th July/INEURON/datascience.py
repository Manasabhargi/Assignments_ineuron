import logging
logging.basicConfig(filename = "test1.log", level = logging.DEBUG, format = '%(message)s')

class ds:
    try:
        def course_ds(self, name, duration):
            self.name = name
            self.duration = duration
            logging.info("Course name is:%s\n duration is %d", self.name, self.duration)
    except Exception as e:
        logging.exception(e)

obds = ds()
obds.course_ds("CS",6)