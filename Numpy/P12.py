import numpy as np 
arr = np.array([12, 45, 67, 23, 89, 34, 90, 15])
print(arr[arr > 50])

print(arr[arr < 30])

print(arr[(arr > 20) & (arr < 80)])

print(arr[arr >= 45])