#arrays are commonly created from python lists

#create a numpy array
import numpy as np
numbers = np.array([10,20,30,40])
#print(numbers)

#two dimensional array from nested list
array2 =np.array([[10,20,30,40],[10,20,30,40]])
#print(array2)

#one dimensional array from a tuple
array3 = np.array((10,20,30,40))
#print(array3)

zero_array =np.zeros((4,5))
#print(zero_array)

random_array = np.random.rand(3,6)
#print(random_array)

#mathematical and statistical functions
array5 =np.array([30,50,10])
total= np.sum(array5)
print(total)