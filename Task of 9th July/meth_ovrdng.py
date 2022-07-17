# Python program to demonstrate
# method overriding
import logging

logging.basicConfig(filename = "test1.log", level = logging.DEBUG,  format = "%(message)s")

"""------------------------------1st example------------------------------"""
# Defining parent class
class ineuron():
    try:
        # Constructor
        def __init__(self):
            self.address = "Ineuron office @ Bangalore"

        # Parent class method
        def show_info(self):
         logging.info(self.address)
    except Exception as e:
        logging.exception(e)

# Defining child class
class oneneuron(ineuron):
    try:
        # Constructor
        def __init__(self):
            self.address = "LP Nagar"

        # Child's show method
        def show_info(self):
           logging.info(self.address)
    except Exception as e:
        logging.exception(e)

# Driver's code
obj1 = ineuron()
obj11 = oneneuron()

obj1.show_info()
obj11.show_info()

"""------------------------------2nd example------------------------------"""
class students:
    try:
        def student_info(self):
            logging.info("Display student information")
    except Exception as e:
        logging.exception(e)
class teachers:
    try:
        def display(self):
            logging.info("Display teachers info")
    except Exception as e:
        logging.exception(e)
class stu_tea(students,teachers):
    try:
        def student_info(self):
            logging.info("Display both students and teachers info")
    except Exception as e:
        logging.exception(e)

obj2 = stu_tea()
obj2.student_info()


"""------------------------------3rd example------------------------------"""
class types:
    try:
        def diif_types(self):
            logging.info("Display diff classes")
    except Exception as e:
        logging.exception(e)
class many_types:
    try:
        def display(self):
            logging.info("Display many classes info")
    except Exception as e:
        logging.exception(e)
class cls_types(types,many_types):
    try:
        def diif_types(self):
            logging.info("Display all the class types info")
    except Exception as e:
        logging.exception(e)

obj2 = cls_types()
obj2.diif_types()

"""------------------------------4th example------------------------------"""
class affiliates():
    try:
        # Constructor
        def __init__(self):
            self.aflt = "Ineuron office Affiliate"

        # Parent class method
        def show_info(self):
         logging.info(self.aflt)
    except Exception as e:
        logging.exception(e)

# Defining child class
class oneneuron(affiliates):
    try:
        # Constructor
        def __init__(self):
            self.aflt = "affiliate of ineuron in punjab"

        # Child's show method
        def show_info(self):
           logging.info(self.aflt)
    except Exception as e:
        logging.exception(e)

# Driver's code
obj1 = affiliates()
obj11 = oneneuron()

obj1.show_info()
obj11.show_info()

"""------------------------------5th example------------------------------"""
class internship:
    try:
        def interns(self):
            logging.info("Display interns info")
    except Exception as e:
        logging.exception(e)

class interns(ineuron):
    try:
        def interns(self):
            logging.info("Diff interns method for method overriding")
    except Exception as e:
        logging.exception(e)
obj5 = internship()
obj5.interns()

"""------------------------------6th example------------------------------"""
class blogger:
    try:
        def blogs(self):
            logging.info("Display blog info")
    except Exception as e:
        logging.exception(e)

class interns(blogger):
    try:
        def blogs(self):
            logging.info("Diff interns blog for method overriding")
    except Exception as e:
        logging.exception(e)
obj5 = blogger()
obj5.blogs()

"""------------------------------7th example------------------------------"""
class jobs:
    try:
        def job(self):
            logging.info("Display job info")
    except Exception as e:
        logging.exception(e)

class job_type(jobs):
    try:
        def job(self):
            logging.info("Diff jobs for method overriding")
    except Exception as e:
        logging.exception(e)
obj5 = job_type()
obj5.job()

"""------------------------------8th example------------------------------"""
class jobs:
    try:
        def job(self):
            logging.info("Display job info")
    except Exception as e:
        logging.exception(e)

class job_type(jobs):
    try:
        super().job()
        logging.info("Diff jobs for method overriding")
    except Exception as e:
        logging.exception(e)
obj5 = job_type()
obj5.job()


"""------------------------------9th example------------------------------"""
class ineuron():
    try:
        # Constructor
        def __init__(self):
            self.address = "Ineuron office @ Bangalore"

        # Parent class method
        def sstudent(self):
         logging.info(self.address)
    except Exception as e:
        logging.exception(e)

# Defining child class
class afiliate(ineuron):
    try:
        # Constructor
        def __init__(self):
            self.address = "LP Nagar"

        # Child's show method
        def intern(self):
           logging.info(self.address)
        def sstudent(self):
         logging.info(self.address)
    except Exception as e:
        logging.exception(e)

# Driver's code
obj1 = ineuron()
obj11 = afiliate()

obj11.intern()
obj11.sstudent()


"""------------------------------10th example------------------------------"""
class ineuron:
    try:
        def acheiver(self):
            logging.info("Display acheivers info")
    except Exception as e:
        logging.exception(e)

class hall_of_fame(ineuron):
    try:
        super().acheiver()
        logging.info("Diff acheivers info for method overriding")
    except Exception as e:
        logging.exception(e)
obj10 = hall_of_fame()
obj10.acheiver()

