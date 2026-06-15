#write a program demonstrating the difference between local and global variables
x= 10

def my_function():
    y = 20
    print("Inside function - Global variable:", x)
    print("Inside function - Local variable:", y)

my_function()
print("Outside function - Global variable:", x)
