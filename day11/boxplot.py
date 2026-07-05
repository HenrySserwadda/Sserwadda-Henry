import matplotlib.pyplot as plt

data=[[20,10,12,15,14,24],[8,9,10,12,13,14,16],[13,14,15,16,17,18,20]]
plt.boxplot(data)
plt.title("Boxplot")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()    