class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'HELLO'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  #super()로 기반 클래스(Person)의 __init__ 메서드 호
        self.school = 'coding dojang'

james = Student()
print(james.school)
print(james.hello)
