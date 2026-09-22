import numpy as np
marks = np.array([78,92,65, 88, 95, 71, 84])
print ("Highest max",np.max(marks))
print ("index of highest mark",np.argmax(marks))
print ("lowest marks",np.min(marks))
print ("Index of lowest mark",np.argmin(marks))
print ("Average" ,np.mean(marks))
s= np.argmax(marks)+1
print ("Student Position",s)
