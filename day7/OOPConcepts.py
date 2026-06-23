class Student:
    def __init__(self, name,age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number

student1 = Student("Henry", 22, "S12345")
print(student1.name)        