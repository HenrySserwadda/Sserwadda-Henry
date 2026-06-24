#it's inheriting attributes and methods from another class (parent or base class)
class Animal:
    def __init__(self, name):
        self.name = name
        #self.breed = breed

    def info(self):
        print("Animal name:", self.name)

    #create a child class that inherits from the Animal class
class Dog(Animal):
    def sound(self):
        print(self.name, "banks")

w= Dog("Buddy")
w.info()
w.sound()                