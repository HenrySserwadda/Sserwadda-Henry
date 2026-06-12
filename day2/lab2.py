score =int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
    print("Excellent! You got an A.")
elif score >= 80:
    grade = 'B'
    print("Good job! You got a B.")
elif score >= 70:
    grade = 'C'
    print("You passed! You got a C.")
else:
    grade = 'D'
    print("You failed. You got a D.")


