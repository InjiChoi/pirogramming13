class Person:
    def greeting(self):
        print('Hello')

class Student(Person):
    def greeting(self):
        super().greeting() # 기반 클래스의 메서드 호출로 중복을 줄임
        print('hello, I`m student.')

james = Student()
james.greeting()
