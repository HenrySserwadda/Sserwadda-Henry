#switch case example using if-elif-else statements on grades
grade = input("Enter the student's grade: ")

match grade:
    case 'A':
        print("Excellent! You got an A.")
    case 'B':
        print("Good job! You got a B.")
    case 'C':
        print("You passed! You got a C.")
    case _:
        print("You failed. You got a D.")