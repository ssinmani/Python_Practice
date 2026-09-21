import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.shape) # o/p 12 as the orginal array id 1D
print(arr.reshape(3,4))
c= arr.reshape(3,4)
print(c.shape) # o/p is tpred in C after reshape so it shows (3,4)



