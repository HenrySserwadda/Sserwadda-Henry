#simple bar chart
import matplotlib.pyplot as plt
w=['John','Mary','Peter','David']
z=[20,30,40,50]

plt.bar(w,z)
plt.title("Simple Bar Chart")
plt.xlabel("Names of students")
plt.ylabel("Marks of students")
plt.show()