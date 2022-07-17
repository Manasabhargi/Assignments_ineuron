"""10 diff examples for the concept of Public variables and methods"""
import logging
logging.basicConfig(filename = "test7.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""
#public attributes
class ineuron:
    employee = 'Manasa'
    try:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    except Exception as e:
        logging.exception(e)

obj1 = ineuron("Madhu",28)
logging.info(obj1.employee)
obj1.name
obj1.age = 28

"""------------------------------2nd example------------------------------"""
class students:
    try:
        def __init__(self,batch):
            self.batch = batch
    except Exception as e:
        logging.exception(e)
obj2 = students("2nd")
obj2.batch


"""------------------------------3rd example------------------------------"""
class types:
    type_name = 'xyz'
    try:
        def __init__(self):
            self.type_name = 'TypeA'
        def type(self):
            logging.info("The diff types are displayed")
    except Exception as e:
        logging.exception(e)
obj3 = types()
obj3.type_name
obj3.type()


"""------------------------------4th example------------------------------"""
class Affiliates:
    afl1 = 0
    afl2 = 0
    try:
        def afflt(self,afl1,afl2):
            self.afl1 = afl1
            self.afl2 = afl2
        def affl_display(self):
            logging.info(self.afl1)
    except Exception as e:
        logging.exception(e)
obj4 = Affiliates()
obj4.afl1
obj4.affl_display()


"""------------------------------5th example------------------------------"""
class blog:
    try:
        def __init__(self,public,pvt):
            self.public = public
            self.pvt = pvt
        def display_blog(self):
            logging.info("the contents of the blog are")
    except Exception as e:
        logging.exception(e)
obj5 = blog("abc","xyz")
obj5.display_blog()


"""------------------------------6th example------------------------------"""
class Internship:
    inter = 20
    try:
        def intern_info(self,name,address):
            self.name = name
            self.address = address
    except Exception as e:
        logging.exception(e)
obj6 = Internship()
obj6.intern_info("Dhanvi","London")


"""------------------------------7th example------------------------------"""
class jobs:
    try:
        def __init__(self):
            pass
        def job_info(self,title):
            self.title = title
            logging.info(self.title)
    except Exception as e:
        logging.exception(e)
obj7 = jobs()
obj7.job_info("coder")


"""------------------------------8th example------------------------------"""
class DataScience:
    ds = 0
    try:
        def course(self,name):
            self.name = name
        def info(self):
            logging.info("Couse namme is Data Science")
    except Exceptiona as e:
        logging.exception(e)
obj8 = DataScience()
obj8.info()


"""------------------------------9th example------------------------------"""
class students:
    name = 'xyz'
    age = 0
    try:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def students_info(self):
            logging.info("The students are:" + str(self.name))
    except Exception as e:
        logging.exception(e)
obj9 = students("Sourabh",30)
obj9.students_info()


"""------------------------------10th example------------------------------"""
class typeA:
    a = 0
    b = 0
    try:
        def classtype(self):
            pass
        def classname(self,name):
            self.name = name
            logging.info(self.a)
    except Exception as e:
        logging.exception(e)
obj10 = typeA()
obj10.classname("Manasa")




