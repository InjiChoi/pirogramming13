class A:
    def greeting(self):
        print('hello im A')

class B(A):
    def greeting(self):
        print('hello im B')

class C(A):
    def greeting(self):
        print('hello im C')

class D(B,C):
        pass
x=D()
x.greeting()
