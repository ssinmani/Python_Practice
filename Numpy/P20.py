import numpy as np
scores = np.array([
    [80, 75, 90],
    [60, 55, 70],
    [95, 88, 92],
    [45, 50, 40]
])

print("Average score of each student",np.mean(scores,axis=1))
print ("Average score of each subject" ,np.mean(scores,axis=0))
s= np.mean(scores,axis=1)
print ("Students whose avgerage greater thna 80",s[s>80])
print ("Overall Maximun score",np.max(scores))
print ("Overall Maximun score",np.min(scores))

