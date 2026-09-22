import numpy as np 
arr= np.array ([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])

print (arr[0:2 :])  # - start at row 0 and stop before row 2 .therfore get 0 and 1
print (arr[:,2:4])
print (arr[1:3,1:3])
print (arr[0,2:4])


