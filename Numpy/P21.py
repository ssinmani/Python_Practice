import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print ("Array is ",np.concatenate((a,b)))
print ("Stack a and b ",np.vstack((a,b)))
print ("Stack a and b ",np.hstack ((a,b)))