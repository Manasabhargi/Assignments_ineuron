"""10 diff examples for the concept of Encapsulation"""
import logging
logging.basicConfig(filename = "test4.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""
#creating a base class
class course:
    try:
        def __init__(self):
            self._a = 2     #protected member
    except Exception as e:
        logging.exception(e)

#creating a derived class
class no_of_courses(course):
    try:
        def __init__(self):
            course.__init__(self)       #calling constructor of base class course
            logging.info("Calling protected member of base class:" + str(self._a))

            self._a = 3         #modify the protected variable
            logging.info("Calling modified protected member outside the class" + str(self._a))
    except Exception as e:
        logging.exception(e)

obj1 = course()
obj11 = no_of_courses()

"""------------------------------2nd example------------------------------"""
#Encapsulation using public members
class student:
    try:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def Age(self):
            logging.info("Age:%d",self.age)
    except Exception as e:
        logging.exception(e)

obj2 = student("Manasa",28)
logging.info(obj2.name)
obj2.Age()

"""------------------------------3rd example------------------------------"""
#Encapsulation using private members
class jobs:
    __fulltime = 0
    __parttime = 0
    try:
        def __init__(self):
            self.__fulltime = 10
            self.__parttime = 20
            logging.info("Available full time jobs are:" + str(self.__fulltime))
            logging.info("Available part time jobs are:" + str(self.__parttime))
    except Exception as e:
        logging.exception(e)
obj3 = jobs()
logging.info(obj3._jobs__fulltime)
logging.info(obj3._jobs__parttime)

"""------------------------------4th example example------------------------------"""
#Encapsulation using protected members
class details:
    _name = "Sudhanshu"
    _age = 31
    _job = "Mentor"

class display_details(details):
    try:
        def __init__(self):
            logging.info("Name is %s\n Age is %d\n Job is %s",self._name,self._age,self._job)
    except Exception as e:
        logging.exception(e)

obj4 = display_details()
logging.info(obj4._name)
logging.info(obj4._age)

"""------------------------------5th example example------------------------------"""
class no_of_courses:
    try:
        def __init__(self):
            self.current = 0
        def increment(self):
            self.current += 1
        def value(self):
            logging.info(self.current)
        def reset(self):
            self.current = 0
    except Exception as e:
        logging.exception(e)
obj5 = no_of_courses()
obj5.increment()
obj5.increment()
obj5.value()

"""------------------------------6th example example------------------------------"""
class ineuron:
    try:
        def __init__(self):
            self.current = 0
        def affiliates(self):
            self.current += 1
        def Interns(self):
            logging.info(self.current)
        #def reset(self):
         #   self.current = 0
    except Exception as e:
        logging.exception(e)
obj6 = ineuron()
obj6.affiliates()
obj6.Interns()

"""------------------------------7th example example------------------------------"""
class students:
    try:
        def __init__(self,name,course,project):
            self.name = name
            self.course = course
            self.project = project
        def student_details(self):
            logging.info("Name is %s\n Student course is %s\n And the student working on project:"+ str(self.name) + str(self.course) + str(self.project))
        def work(self):
            logging.info(self.name)
            return self.name
    except Exception as e:
        logging.exception(e)
obj7 = students("Mansa","CS","Data Science")
obj7.student_details()
obj7.work()

"""------------------------------8th example------------------------------"""
class blogs:
    try:
        def __init__(self,name,content):
            self.name = name
            self.content = content
        def display_contents(self):
            logging.info("The contents of the blog is " + str(self.content))
    except Exception as e:
        logging.exception(e)
obj8 = blogs("Manasa","ABC")
logging.info(obj8.name)
obj8.display_contents()

"""------------------------------9th example example------------------------------"""
class jobs:
    try:
        def __init__(self):
            self.a = 123
            self._b = 123
            self.__c = 123
    except Exception as e:
        logging.exception(e)
obj9 = jobs()
logging.info(obj9.a)
logging.info(obj9._b)
logging.info(obj9._jobs__c)

"""------------------------------10th example example------------------------------"""
class inueron:
    try:
        def __init__(self,typeA,typeB):
            self.typeA = typeA
            self.typeB = typeB
        def classtype(self):
            logging.info(self.typeA)
            logging.info(self.typeB)
    except Exception as e:
        logging.exception(e)
obj10 = inueron("CS","EC")
obj10.classtype()













