import numpy as np

arr = np.arange(1, 13)
print ("Spilt array",np.split(arr,3))

s= np.split(arr,3)
print ("Mean is ",np.mean(s[0]))
print ("Mean is ",np.mean(s[1]))
print ("Mean is ",np.mean(s[2]))
