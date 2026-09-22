import numpy as np 

energy = np.array([12, 15, 11, 18, 20, 17, 14, 22, 19, 16])

print ("Total is" ,np.sum(energy))
print ("Mean Consumption",np.mean(energy))
print ("Minimum is ",np.min(energy))
print ("Maximum is ",np.max(energy))
print("Standard Deviation",np.std(energy))
print ("Values Greater than 18 is",energy[energy>18])
print ("Count of Value greater than 18 ", np.sum(energy>18))
print ("Range is ",max(energy)- min(energy))
