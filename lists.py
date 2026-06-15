#creating a list
Food=["Posho","Rice","Beans","Chapati"]
print(Food)
print(type(Food))

#accessing list items
print(Food[0])

#adding items to a list
Food.append("Sukuma")
print(Food)

#add an item at a specific index
Food.insert(1,"Matoke")
print(Food)

#use of a constructor to create a list
Food2=list(("Posho","Rice","Beans","Chapati"))
print(Food2)