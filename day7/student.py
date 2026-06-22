# create class Student
class Student:
    name = "Henry"
    Nationality = "Ugandan"

    # using the __init__ method to initialize the class
    def __init__(self, age, religon):
        self.age = age
        self.religon = religon

# create an object of the class Student
student1 = Student(22, "Christian")
print(student1.name)