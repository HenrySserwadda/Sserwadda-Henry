import csv

data = [
    ["Name", "Age", "Course"],
    ["Henry", 22, "Computer Science"],
    ["Sarah", 21, "Information Technology"],
    ["John", 23, "Software Engineering"],
    ["Grace", 20, "Data Science"],
    ["David", 24, "Cyber Security"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv created successfully!")