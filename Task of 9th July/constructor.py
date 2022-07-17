"""10 diff examples for the concept of constructors"""

""" 1st example"""
import logging
logging.basicConfig(filename="test1.log",level = logging.DEBUG, format = '%(name)s %(message)s')

class ineuron:
    try:
        def __init__(self):
            self.subject = "Data Science"

        def print_subject(self):
            logging.info(self.subject)
    except Exception as e:
        logging.exception(e)

obj = ineuron()
obj.print_subject()

"""------------------------2nd example---------------------"""

class internship:
    try:
        def __init__(self):
            self.course = "Computer Science and Engineering"
        def print_course(self):
            logging.info(self.course)
    except Exception as e:
        logging.info(e)

obj2 = internship()
obj2.print_course()

"""--------------------3rd example--------------------"""

class students:
    courseA = 0
    courseB = 0
    Total = 0
    try:
        def __init__(self,A,B):
            self.courseA = A
            self.courseB = B
        def number_of_courses(self):
            logging.info("Students in course A =" + str(self.courseA))
            logging.info("Students in course B =" + str(self.courseB))
            logging.info("Total Students =" + str(self.Total))
        def calculate(self):
            self.Total = self.courseA + self.courseB
    except Exception as e:
        logging.exception(e)

obj3 = students(200,300)
obj3.calculate()
obj3.number_of_courses()

"""--------------------4th example--------------------"""

class jobs:
    tech_jobs = 0
    nontech_jobs = 0
    total = 0
    try:
        def __init__(self,t,n):
            self.tech_jobs = t
            self.nontech_jobs = n
        def print_total_jobs(self):
            logging.info("Available tech jobs are" + str(self.tech_jobs))
            logging.info("Available non tech jobs are" + str(self.nontech_jobs))
            logging.info("Total jobs available are" + str(self.total))
        def total_jobs(self):
            self.total = self.tech_jobs + self.nontech_jobs
    except Exception as e:
        logging.exception(e)

obj4 = jobs(500,400)
obj4.total_jobs()
obj4.print_total_jobs()

"""--------------------5th example--------------------"""

class Affiliates:
    try:
        def __init__(self,name,id):
            self.id = id
            self.name = name
        def affiliate_info(self):
            logging.info("ID: %d\n Name: %s" %(self.id, self.name))
    except Exception as e:
        logging.exception(e)

afl1 = Affiliates("John",1)
afl2 = Affiliates("David",2)
afl3 = Affiliates("Smith",3)

afl1.affiliate_info()
afl2.affiliate_info()
afl3.affiliate_info()

"""--------------------6th example--------------------"""

class Students:
    count = 0
    try:
        def __init__(self):
            Students.count = Students.count + 1
    except Exception as e:
        logging.exception(e)
st1 = Students()
st2 = Students()
st3 = Students()
logging.info("Total number of students:" + str(Students.count))

"""--------------------7th example--------------------"""

class blog:
    try:
        def __init__(self):
            logging.info("This is to display the blog owner's name")
        def display(self,name):
            logging.info("The owner of this blog is:%s", name)
    except Exception as e:
        logging.exception(e)

obj7 = blog()
obj7.display("Sudh")

"""--------------------8th example--------------------"""

class courses:
    sub_code = 84
    sub_name = "Computer Science"
    try:
        def display(self):
            logging.info("%d\n %s", self.sub_code, self.sub_name)
    except Exception as e:
        logging.exception(e)

obj8 = courses()
obj8.display()

"""--------------------9th example--------------------"""
"""If there are 2 diff constructors in the same class, then the object will always call last constructor"""

class ineuron:
    try:
        def __init__(self):
            logging.info("The first course in ineuron:")
        def __init__(self):
            logging.info("The second course in ineuron:")
    except Exception as e:
        logging.exception(e)

obj9 = ineuron()

"""--------------------10th example--------------------"""

class Student:
    try:
        def __init__(self,name,id,age):
            self.name = name
            self.id = id
            self.age = age
        def display_details(self):
            logging.info("Name:%s, ID:%d, age:%d" %(self.name, self.id, self.age))
    except Exception as e:
        logging.exception(e)

obj10 = Student("JOHN",11,28)
logging.info(obj10.__doc__)
logging.info(obj10.__dict__)
logging.info(obj10.__module__)