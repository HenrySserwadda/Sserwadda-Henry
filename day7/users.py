class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)

    def greet_user(self):
        print("Hello,", self.first_name + "!")


user1 = User("Henry", "Sserwadda", 22, "henry@gmail.com")
user2 = User("John", "Doe", 25, "john@gmail.com")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()