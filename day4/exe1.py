#write a function that takes in input and calculates the area  of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area 

x = int(input("Enter the length of the rectangle: "))
y = int(input("Enter the width of the rectangle: "))
print("The area of the rectangle is:", area_of_rectangle(x, y))

#what is a parameter in a function?#
# A parameter in a function is a variable that is used to receive a value when the function is called
#arguments are passed to the function. It acts as a placeholder for the value that will be provided when the function is called. Parameters allow functions to be more flexible and reusable, as they can work with different inputs each time they are called.