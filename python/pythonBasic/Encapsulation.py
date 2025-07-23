'''
Encapsulation, Encapsulation describes the idea of wrapping data and the
methods that work on data within one unit. This puts restrictions on
accessing variables and methods directly and can prevent the accidental
modification of data.
'''

class base:
    def __init__(self):
        print('this is __init__ method, gets called whenever class is referenced')
        self.__method2()
    def method1(self):
        print("regular method")
    def __method2(self):
        print("this is private method to base class")

obj=base()
obj.method1()
obj.__method2() ## This is private base class and cannot be called, this is encapsulation