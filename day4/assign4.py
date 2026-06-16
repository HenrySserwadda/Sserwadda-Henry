#create a menu driven calculator using function for addition, subtraction, multiplication
# Functions

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Menu-Driven Calculator
while True:
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Calculator closed.")
        break

    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", addition(num1, num2))

        elif choice == 2:
            print("Result =", subtraction(num1, num2))

        elif choice == 3:
            print("Result =", multiplication(num1, num2))

        elif choice == 4:
            print("Result =", division(num1, num2))

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
