#matplotlib Pyplot is a module that is found within matplotlib that provides a MATLAB
#it simplifies the process of adding plot elements
# basic line graph

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

fig,ax = plt.subplots()
ax.plot(x,y,marker='o',label="Data Points")
ax.set_title("Basic Line Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

ax.legend()
plt.show()