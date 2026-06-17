#both inbuilt and external
#inbuilt can be accessed using the import keyword

import math
pie =math.pi
print("value of pie is",pie)

import pandas

data ={
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
}
df = pandas.DataFrame(data)
print(df)

import math as m
