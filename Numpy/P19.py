import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print ("Sum of each row",np.sum(arr,axis=1))
print ("Sum of each column",np.sum(arr,axis=0))
print ("Mean of each row",np.mean(arr,axis=1))
print ("Mean of each column",np.mean(arr,axis=0))
print ("Minimum of each column",np.min(arr,axis=0))
print ("Maximum of each row",np.max(arr,axis=1))