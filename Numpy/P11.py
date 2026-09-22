import numpy as np 
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 6, 8, 10])

s = arr1+arr2
y = arr1-arr2
z= arr1*arr2
w = arr1/arr2
print ("Total of the array" ,s)
print ("Total of the array" ,y)
print ("Total of the array" ,z)
print ("Total of the array" ,w)
print ("Mean",np.mean(z))