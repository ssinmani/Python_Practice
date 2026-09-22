import numpy as np

temps = np.array([25, 32, 18, 40, 29, 35, 22, 41, 27])

print ("Temperature greater than 30:" ,temps[temps>30])
print ("Temperature less than:" ,temps[temps<25])
temps[temps>35]=35
print ("new array:" ,temps)
print ("new average",np.mean(temps))
print ("Maximum after replacement",np.max(temps))
