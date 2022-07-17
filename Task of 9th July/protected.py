"""10 diff examples for the concept of Protected variables"""
import logging
logging.basicConfig(filename = "test8.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""
class student:
    #protected data members
    _name = None
    _roll = None
    _branch = None
    try:
        def __init__(self,name,roll,branch):
            self._name = name
            self._roll = roll
            self._branch = branch
        #protected member function
        def _displayRollandBranch(self):
            logging.info(self._roll)
            logging.info(self._branch)
    except Exception as e:
        logging.exception(e)

class parent(student):
    try:
        def __init__(self,name,roll,branch):
            student.__init__(self,name,roll,branch)
        def displaydetails(self):
            logging.info("Name is" + str(self._name))
            self._displayRollandBranch()        #accessing protected method
    except Exception as e:
        logging.exception(e)
obj1 = parent("John",123456,"Information Technology")
obj1.displaydetails()


"""------------------------------2nd example------------------------------"""
class ineuron:
    try:
        def __init__(self,name,location):
            self._name = name
            self._location = location
        def _time(self):
            pass
    except Exception as e:
        logging.exception(e)
obj2 = ineuron("oneneuron","Bangalore")
obj2._time()

"""------------------------------3rd example------------------------------"""
class types:
    _typea = None       #protected variable
    try:
        def typeA(self):
            pass
        def _typeB(self):
            logging.info("This is the protected meber function")
    except Exception as e:
        logging.exception(e)
obj3 = types()
obj3._typeB()


"""------------------------------4th example------------------------------"""
class Affiliate:
    try:
        def __init__(self, name, salary):
            self._name = name
            self._salary = salary
    except Exception as e:
        logging.exception(e)
a1=Affiliate("Simon", 12500)
logging.info(a1._name)


"""------------------------------5th example------------------------------"""
class blogs:
    try:
        def __init__(self, blog_name, details):
            self._blog_name = blog_name
            self._details = details
    except Exception as e:
        logging.exception(e)
b1=blogs("Artificial Intelligence", "Hidden contents")
logging.info(b1._blog_name)


"""------------------------------6th example------------------------------"""
class Interns:
    try:
        def __init__(self,name):
            self._intern = name
    except Exception as e:
        logging.exception(e)
obj6 = Interns("Samhitha")
logging.info(obj6._intern)


"""------------------------------7th example------------------------------"""
class jobs:
    _job = None
    try:
        def __init__(self,job_name):
            self._job = job_name
    except Exception as e:
        logging.exception(e)
obj7 = jobs("Teacher")
logging.info(obj7._job)


"""------------------------------8th example------------------------------"""
class ineuron:
    _job = None
    try:
        def __init__(self,job_name):
            self._job = job_name
    except Exception as e:
        logging.exception(e)
obj8 = jobs("Teacher")
logging.info(obj8._job)
obj8._job = "Mentor"        #changing protected variable value
logging.info(obj8._job)


"""------------------------------9th example------------------------------"""
class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        logging.info("This is good " + string)

emp = Employee("harry", 343, "Programmer")
logging.info(emp._Employee__pr)


"""------------------------------10th example------------------------------"""
class INEURON:
    _student = None
    try:
        def ineuron_student(self,name):
            self._student = name
            logging.info(self._student)
    except Exception as e:
        logging.exception(e)
obj10 = INEURON()
obj10.ineuron_student("Manasa")
obj10._student
