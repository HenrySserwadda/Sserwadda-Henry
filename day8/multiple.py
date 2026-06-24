#when a class inherits from more than one base class
#it follows linearization rule
class Class1:
    def w(self):
        print("From Class1")

class Class2(Class1):
    def w(self):
        print("From Class2")

class Class3(Class1):
    def w(self):
        print("From Class3")

class Class4(Class2, Class3):
    pass
obj = Class4()
obj.w()                        