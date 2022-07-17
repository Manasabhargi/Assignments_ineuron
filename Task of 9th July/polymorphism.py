"""10 diff examples for the concept of Polymorphism"""
import logging
logging.basicConfig(filename = "test5.log", level = logging.DEBUG, format = '%(message)s')

"""------------------------------1st example------------------------------"""
class Affiliate1:
    try:
        def name(self):
            logging.info('Manasa')
        def language(self):
            logging.info('Kannada,English and Hindi')
    except Exception as e:
        logging.exception(e)
class Affiliate2:
    try:
        def name(self):
            logging.info('Bhargav')
        def language(self):
            logging.info('Hindi and English')
    except Exception as e:
        logging.exception(e)
obj1 = Affiliate1()
obj11 = Affiliate2()
for affiliates in (obj1,obj11):
    affiliates.name()
    affiliates.language()

"""------------------------------2nd example------------------------------"""
class Intern1:
    try:
        def name(self):
            logging.info('Namitha')
        def duration(self):
            logging.info('4 months')
    except Exception as e:
        logging.exception(e)
class Intern2:
    try:
        def name(self):
            logging.info('Manju')
        def duration(self):
            logging.info('6 months')
    except Exception as e:
        logging.exception(e)
obj2 = Intern1()
obj22 = Intern2()
for internship in (obj2,obj22):
    internship.name()
    internship.duration()

"""------------------------------3rd example------------------------------"""


class Blog1:
    try:
        def name(self):
            logging.info('Manasa')
        def type(self):
            logging.info('official blog')
    except Exception as e:
        logging.exception(e)

class Blog2:
    try:
        def name(self):
            logging.info('Bhargav')
        def type(self):
            logging.info('personal')
    except Exception as e:
        logging.exception(e)

obj3 = Blog1()
obj33 = Blog2()
for bloggers in (obj3, obj33):
    bloggers.name()
    bloggers.type()

"""------------------------------4th example------------------------------"""
class course:
    try:
        def intro(self):
            logging.info("Introduction to the course")
        def project(self):
            logging.info("respective course projects need to be done")
    except Exception as e:
        logging.exception(e)
class CS(course):
    try:
        def project(self):
            logging.info("The CS related projects need to be handeld")
    except Exception as e:
        logging.exception(e)
class EC(course):
    try:
        def project(self):
            logging.info("EC related projects handels here")
    except Exception as e:
        logging.exception(e)

obj4 = course()
obj44 = CS()
obj444 = EC()

obj4.intro()
obj4.project()

obj44.intro()
obj44.project()

obj444.intro()
obj444.project()

"""------------------------------5th example------------------------------"""
def no_of_classes(a,b,c = 0):
    return a + b + c

logging.info(no_of_classes(2,3))
logging.info(no_of_classes(2,3,5))

"""------------------------------6th example------------------------------"""
def no_of_students(x,y,z = 0):
    return x + y + z

logging.info(no_of_students(200,400,500))
logging.info(no_of_students(200,10))


"""------------------------------7th example------------------------------"""
class ineuron():
    try:
        def contact(self):
            logging.info("Bangalore")

        def course(self):
            logging.info("Data Science")

        def type(self):
            logging.info("part time")
    except Exception as e:
        logging.exception(e)

class one_neuron():
    try:
        def contact(self):
            logging.info("Washington, DC")

        def course(self):
            logging.info("Machine Learning")

        def type(self):
            logging.info("Full time")
    except Exception as e:
        logging.exception(e)
try:
    def func(obj7):
        obj7.contact()
        obj7.course()
        obj7.type()

    obj_i = ineuron()
    obj_o = one_neuron()

    func(obj_i)
    func(obj_o)
except Exception as e:
    logging.exception(e)


"""------------------------------8th example------------------------------"""
class Fish():
    try:
        def swim(self):
            logging.info("The Fish is swimming.")
    except Exception as e:
        logging.exception(e)

class Clownfish():
    try:
        def swim(self):
            logging.info("The clownfish is swimming.")
    except Exception as e:
        logging.exception(e)

a = Fish()
a.swim()
b = Clownfish()
b.swim()


"""------------------------------9th example------------------------------"""
class jobs:
    try:
        def job_description(self):
            logging.info("abc")

        def salary(self):
            logging.info("not mentioned")
    except Exception as e:
        logging.exception(e)

class Internship:
    try:
        def job_description(self):
            logging.info("Happy")

        def salary(self):
            logging.info("Woof")
    except Exception as e:
        logging.exception(e)
try:
    obj9 = jobs()
    obj99 = Internship()

    for obj in (obj9, obj99):
        obj.salary()
        obj.job_description()
except Exception as e:
    logging.exception(e)

"""------------------------------10th example------------------------------"""
try:
    def no_of_interns(x, y, z=0):
        return x + y + z
except Exception as e:
    logging.exception(e)

logging.info(no_of_interns(2,4,5))
logging.info(no_of_interns(2,10))





