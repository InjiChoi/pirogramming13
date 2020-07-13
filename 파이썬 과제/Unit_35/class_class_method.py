class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f'{cls.count}명이 생성되었습니다')

james = Person()
maria = Person()

Person.print_count()
