import logging
logging.basicConfig(filename = "test2.log", level = logging.DEBUG, format = '%(message)s')

class ml:
    try:
        def course_ml(self,name,duration):
            self.name = name
            self.duration = duration
            logging.info("Course name is:%s\n duration is %d",self.name,self.duration)
    except Exception as e:
        logging.exception(e)

obml = ml()
obml.course_ml("IT",3)

