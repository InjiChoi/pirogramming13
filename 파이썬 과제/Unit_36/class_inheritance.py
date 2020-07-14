class Person:
    def greeting(self):
        print("Hello")
#is a
class Student(Person):
    def study(self):
        print("study")
#has a
class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)

james = Student()
james.greeting()
james.study()
