class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

#create two methods to increase salary and decrease salary
    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary increased by {amount}. New salary: {self.salary}")

    def decrease_salary(self, amount):
        self.salary -= amount
        print(f"{self.name}'s salary decreased by {amount}. New salary: {self.salary}")
# create an object of the class Employee
employee1 = Employee("Alice", 30, 50000)
employee1.display_employee()
employee1.increase_salary(5000)        