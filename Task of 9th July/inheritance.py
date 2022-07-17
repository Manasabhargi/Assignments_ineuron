"""10 diff examples for the concept of Inheritance"""

"""---------------------1st example--------------------"""

import logging
logging.basicConfig(filename = "test2.log",level = logging.DEBUG, format = '%(message)s')

class Job:
    try:
        def Fulltime(self):
            logging.info("This job is full time work")
    except Exception as e:
        logging.exception(e)
#child class Internship inherits the base class Job
class Internship(Job):
    try:
        def parttime(self):
            logging.info("This Intership is a part time work")
    except Exception as e:
        logging.exception(e)

obj1 = Internship()
obj1.parttime()
obj1.Fulltime()


"""--------------------2nd example--------------------"""
"""multilevel inheritance"""

class ineuron:
    try:
        def number_of_courses(self):
            logging.info("The total available courses are 60")
    except Exception as e:
        logging.exception(e)

class Students(ineuron):
    try:
        def enrolled_students(self):
            logging.info("The total students enrolled for diff courses are 700")
    except Exception as e:
        logging.exception(e)

class class_type(Students):
    try:
        def classes(selfs):
            logging.info("there are diff class numbers available for diff students from 1-10")
    except Exception as e:
        logging.exception(e)

obj2 = class_type()
obj2.classes()
obj2.number_of_courses()
obj2.enrolled_students()


"""--------------------3rd example--------------------"""
#Multiple Inheritance

class food_blogs:
    try:
        def foodies(self):
            logging.info("Different reciepes of south Indian meal")
    except Exception as e:
        logging.exception(e)

class travel_blogs:
    try:
        def tourist(self):
            logging.info("Diff places to visit in India")
    except Exception as e:
        logging.exception(e)

class personal_blog(food_blogs,travel_blogs):
    try:
        def personal(self):
            logging.info("This blog contains info about my personal information")
    except Exception as e:
        logging.exception(e)

obj3 = personal_blog()
obj3.foodies()
obj3.tourist()
obj3.personal()


"""-------------------4h example--------------------"""
"""issubclass method is used to check the relationshipbetween derived and parent class"""

class calculation1:
    try:
        def Summation(self,a,b):
            return a+b
    except Exception as e:
        logging.exception(e)

class calculation2:
    try:
        def Multiplication(self,a,b):
            return a*b
    except Exception as e:
        logging.exception(e)

class Derived(calculation1,calculation2):
    try:
        def Divide(self,a,b):
            return a/b
    except Exception as e:
        logging.exception(e)

obj4 = Derived()
obj4.Summation(10,20)
obj4.Multiplication(10,20)
obj4.Divide(10,20)
logging.info(issubclass(Derived,calculation1))
logging.info(issubclass(calculation1,calculation2))


"""--------------------5th example--------------------"""

class typeA:
    try:
        def A(self):
            logging.info("This is the class section labeled A")
    except Exception as e:
        logging.exception(e)

class typeB:
    try:
        def B(self):
            logging.info("This is the class section labeled B")
    except Exception as e:
        logging.exception(e)

class typeC:
    try:
        def C(self):
            logging.info("This is the class section labeled C")
    except Exception as e:
        logging.exception(e)

class Derived(typeA,typeB,typeC):
    try:
        def section(self):
            logging.info("This is the combined section")
    except Exception as e:
        logging.exception(e)

obj5 = Derived()
obj5.C()


"""--------------------6th example--------------------"""

class courses:
    no_of_courses = 0
    try:
        def __init__(self,no_of_courses):
            self.no_of_courses1 = no_of_courses
    except Exception as e:
        logging.exception(e)

class ineuron(courses):
    try:
        def course(self):
            logging.info("the total no of courses are: %s" + str(self.no_of_courses))
    except Exception as e:
        logging.exception(e)

obj6 = ineuron(3)
obj6.course()


"""--------------------7th example--------------------"""

class Affiliate(object):
    try:
        def __init__(self,name):
            self.name = name
        def getname(self):
            logging.info("The name of the affiliate is:%s", self.name)
        def isEmployee(self):
            return False
    except Exception as e:
        logging.exception(e)

class ineuron(Affiliate):
    try:
        def isEmployee(self):
            return True
    except Exception as e:
        logging.exception(e)

obj7 = Affiliate("John")
obj7.getname()
obj7.isEmployee()


obj77 = ineuron("Smith")
obj77.isEmployee()
obj77.getname()


"""--------------------8th example--------------------"""

class Internship:
    try:
        def Intern_info(self, name, age):
            logging.info("name:%s, age:%d", name, age)
    except Exception  as e:
        logging.exception(e)

class ineuron:
    try:
        def company_info(self,company_name,location):
            logging.info("Company name is:%s\n Location:%s",company_name,location)
    except Exception as e:
        logging.exception(e)

class Employee(Internship,ineuron):
    try:
        def Employee_info(self,salary,skill):
            logging.info("Salary of employee:%d\n Skillset: %s",salary,skill)
    except Exception as e:
        logging.exception(e)

obj8 = Employee()
obj8.Intern_info("Manasa",28)
obj8.company_info("Ineuron","Bangalore")
obj8.Employee_info(100,"Python")


"""--------------------9th example----------------------"""

class ineuron:
    try:
        def info(self):
            return 'INEURON'
    except Exception as e:
        logging.exception(e)

class student(ineuron):
    try:
        def student_info(self):
            #calling the superclass method using Super() function
            s_name = super().info()
            logging.info("This student studies at :%s",s_name)
    except Exception as e:
        logging.exception(e)

obj9 = student()
obj9.student_info()


"""--------------------10TH EXAMPLE--------------------"""

class ineuron:
    try:
        def __init__(self,address):
            self.address = address
    except Exception as e:
        logging.exception(e)

class student(ineuron):
    try:
        def __init__(self,name):
            self.name = name
    except Exception as e:
        logging.exception(e)

class course(student):
    try:
        def __init__(self,course_name):
            self.course_name = course_name
        def display(self,name,address,course_name):
            logging.info("Student name is %s", name)
            logging.info("Address is :%s",address)
            logging.info("Student enrolled for course:%s",course_name)
    except Exception as e:
        logging.exception(e)

obj10 = course("cse")
obj10.display("Manasa","Bangalore","cse")

