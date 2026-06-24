class Animal:
    def __init__(self,name):
        self.name =name
    def info(self):
        print("Animal name", self.name)

#define child class
class Dog(Animal):
    def __init__(self,name,breed):


#using the super function                    
     super().__init__(name)
self.breed=breed
def details(self):
    print(self.name, "is a",self.breed)

z= Dog("Buddy", "Diamond")
z.info()
z.details()