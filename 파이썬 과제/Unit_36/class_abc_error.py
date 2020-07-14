from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('study')
    def go_to_school(self):
        print('go to school')

james=Student()
james.study()
james.go_to_school()
