"""10 diff examples for the concept of Private variables"""
import logging
logging.basicConfig(filename = "test6.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""
class ineuron:
    __course = "cs"
    try:
        def __students(self):
            logging.info("students enrolled for course cs")
    except Exception as e:
        logging.exception(e)
obj1 = ineuron()
obj1._ineuron__students()
#outside the class if you call private variable __course it will not work

"""------------------------------2nd example------------------------------"""
class students:
    try:
        def __csstudents(self):
            logging.info("Students from cs department")
        def ecstudents(self):
            logging.info("Students from ec department")
    except Exception as e:
        logging.exception(e)
obj2 = students()
obj2.ecstudents()
obj2._students__csstudents()

"""------------------------------3rd example------------------------------"""
class typeA:
    try:
        def __init__(self):
            self.__classtype = None
    except Exception as e:
        logging.exception(e)
class typeB(typeA):
    try:
        def __init__(self):
            self.__classtype = "Regular"
    except Exception as e:
        logging.exception(e)

"""------------------------------4th example------------------------------"""
class courses:
    try:
        def __init__(self,str):
            logging.info("Simple Constructor")
            self.__cs = str
        def no_of_courses(self):
            logging.info(self.__cs)
        def display(self):
            logging.info(self.no_of_courses())
    except Exception as e:
        logging.exception(e)
obj4 = courses("CS")
obj4.no_of_courses()

"""------------------------------5th example------------------------------"""
class Affiliate:
    __term = 0
    try:
        def ineuron(self):
            self.__term = __term
        def display(self):
            logging.info(self.__term)
    except Exception as e:
        logging.exception(e)
obj5 = Affiliate()
obj5.display()

"""------------------------------6th example------------------------------"""
class Internship:
    try:
        def intern(self):
            logging.info("This intern duration is  months")
        def __intern(self):
            logging.info("duration is 6 months")
    except Exception as e:
        logging.exception(e)
class Interns(Internship):
    try:
        def __init__(self):
            Internship.__init__(self)
        def Intern1(self):
            self.intern()
            logging.info("first intern")
        def Intern2(self):
            self._Internship__intern()
            logging.info("second intern")
    except Exception as e:
        logging.exception(e)
obj6 = Internship()
obj6.intern()
obj66 = Interns()
obj66.Intern1()
obj66.Intern2()


"""------------------------------7th example------------------------------"""
class blog:
    try:
        def blog_owner(self):
            logging.info("Contains info about the owner of the blog")
        def __blog_owner(self):
            logging.info("The private info is not displayed to anyone")
        def blog_check(self):
            self.blog_owner()
            self._blog__blog_owner()
    except Exception as e:
        logging.exception(e)
obj7 = blog()
obj7.blog_check()


"""------------------------------8th example------------------------------"""
class jobs:
    try:
        def job1(self):
            logging.info("Available jobs description")
        def __job1(self):           #private method
            logging.info("Private job information")
        def jod_display(self):
            self.job1()
            self._jobs__job1
    except Exception as e:
        logging.exception(e)
obj8 = jobs()
obj8.jod_display()
obj8._jobs__job1         #calling private method

"""------------------------------9th example------------------------------"""
class ineuron:
    try:
        def address(self):
            logging.info("Detailed address is available here")
        def __address(self):            #private method
            logging.info("Detailed address can not be shown")
    except Exception as e:
        logging.exception(e)
obj9 = ineuron()
obj9.address()
obj9._ineuron__address()


"""------------------------------10th example------------------------------"""
class students:
    name = ''
    age = 0
    try:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def attendance(self):
            logging.info("Full 100% attendance")
        def __marks(self):
            logging.info("Marks is")
    except Exception as e:
        logging.exception(e)
obj10 = students("Manasa",28)
obj10._students__marks







