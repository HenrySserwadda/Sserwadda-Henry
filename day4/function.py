#defining a function called greet that takes one parameter, name
def greet(name):
    print("Hello, " + name + "!")
greet("Henry")

#return statements
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print("The sum is:", result)

#return multiple values
def calculate(a, b):
    sum = a + b
    difference = a - b
    return sum, difference
print("The sum and difference are:", calculate(10, 5))
