"""10 diff examples for the concept of Abstraction"""
import logging
logging.basicConfig(filename = "test3.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""

class jobs:
    try:
        def Internship(self):
            pass
    except Exception as e:
        logging.exception(e)

class jobs_Internship:
    try:
        def Internship(self):
            logging.info("Internship for the period of 1 year")
    except Exception as e:
        logging.exception(e)

obj1 = jobs_Internship()
obj1.Internship()


"""------------------------------2nd example------------------------------"""
class ineuron(jobs_Internship):
    try:
        def Affiliate(self):
            pass
    except Exception as e:
        logging.exception(e)

class Ineuron(ineuron):
    try:
        def Affiliate(self):
            logging.info("Affiliated to ineuron")
    except Exception as e:
        logging.exception(e)

obj2 = Ineuron()
obj2.Affiliate()

"""------------------------------3rd example------------------------------"""
class ineuron:
    __students = "data science"
    try:
        def students(self):
            logging.info("Print the class of students", ineuron.__students)
    except Exception as e:
        logging.exception(e)

i = ineuron()
"""since __students is a private variable we need to append class name for that"""
i._ineuron__students


"""------------------------------4th example------------------------------"""
class ABC:
    type1 = 0
    type2 = 0
    try:
        def class_type(self,type1,type2):
            logging.info("There are two types of class:%s, %s", type1, type2)
    except Exception as e:
        logging.exception(e)

obj4 = ABC()
obj4.class_type("A","B")

"""------------------------------5th example------------------------------"""
class ineuron:
    try:
        def no_of_courses(self):
            logging.info("There are 200+ courses available")
        def ineuron(self):
            pass
    except Exception as e:
        logging.exception(e)

obj5 = ineuron()
obj5.no_of_courses()

"""------------------------------6th example------------------------------"""
class educlass:
    try:
        def class_type(self,a):
            logging.info("The class type is:",a)
        def course(self):
            logging.info("Data Science")
    except Exception as e:
        logging.exception(e)

class student:
    try:
        def course(self):
            logging.info("Machine Learning")
        def classtype(self):
            pass
    except Exception as e:
        logging.exception(e)

obj6 = student()
obj6.course()

"""------------------------------7th example------------------------------"""
class Internship:
    try:
        def certificate(self):
            pass
    except Exception as e:
        logging.exception(e)

class Intern(Internship):
    try:
        def Intern_name(self,name):
            logging.info("Intern name is:",name)
        def certificate(self,name):
            logging.info("Certificate issued for Intern %s",name)
    except Exception as e:
        logging.exception(e)

obj7 = Intern()
obj7.certificate("Manasa")

"""------------------------------8th example------------------------------"""
class blog:
    blog_name = "ML"
    try:
        def own_blog(self):
            logging.info("Blog name is : %s", blog.blog_name)
    except Exception as e:
        logging.exception(e)

obj8 = blog()
obj8.own_blog()

"""------------------------------9th example------------------------------"""
class ABCclass:
    try:
        def class_name(self,name):
            logging.info("Class name is:%s",name)
        def abs_class(self):
            logging.info("This is the abstract method")
    except Exception as e:
        logging.exception(e)

class testclass(ABCclass):
    try:
        def abs_class(self):
            logging.info("Abstract methos overirded")
    except Exception as e:
        logging.exception(e)

obj9 = testclass()
obj9.abs_class()
logging.info("obj9 is instance of class ABCclass    " + str(isinstance(obj9,ABCclass)))

"""------------------------------10th example------------------------------"""
class ineuron:
    try:
        def classA(self): #abstract method
            pass
        def print_class(self):   #normal method
            logging.info(self.classA)
    except Exception as e:
        logging.exception(e)

class batch(ineuron):
    #classA = 0
    try:
        logging.info("Hi")
    except Exception as e:
        logging.exception(e)

obj10 = batch()
obj10.classA()          #overriding abstract method







