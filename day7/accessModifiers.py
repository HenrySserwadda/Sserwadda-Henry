#acess modifiers are used to restrict access to methods and variables. In python, we use underscore to define access modifiers. There are three types of access modifiers in python:
#1. Public access modifier: This is the default access modifier in python. It allows access to methods and variables from anywhere in the program. Public methods and variables are defined without any underscore.
#2. Protected access modifier: This access modifier allows access to methods and variables within the class and its subclasses. Protected methods and variables are defined with a single underscore.
#3. Private access modifier: This access modifier allows access to methods and variables only within the class itself. Private methods and variables are defined with a double underscore.
''''
class Employee:
    def __init__(self):
        self.name ='Henry'#public variable

employee1 = Employee()
print(employee1.name)
'''       


class Employee:
    def __init__(self):
        self.__salary  =600000#private variable

employee1 = Employee()
print(employee1.__salary)        