#these store information in key value pairs  
#WITHOUT THE DICT FUNCTION
data ={
    "x":1,
    "y":30
}
print(data)

#using dict function
b = dict(name ="Sam", age =17)
print(b)

#accessing dictionary items
print(b["name"])

#using get method
print(b.get("age"))

#adding and updating dictionary items
b["cgpa"] =4.5
print(b)

b["name"]= "Henry"
print(b)

#removing dictionary items
del b["age"]
print(b)

#using pop() method
