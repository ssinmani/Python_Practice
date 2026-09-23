import numpy as np
waiting_time = np.array([
    32, 45, 28, 51, 63,
    37, 42, 29, 55, 71,
    38, 46, 52, 31, 68
])
s=np.mean(waiting_time)
m=np.sum(waiting_time > 50)/np.sum(waiting_time) * 100
#Basic Analysis
print("Total:",np.sum(waiting_time))
print("Average:",np.mean(waiting_time))
print("Maximum:",np.max(waiting_time))
print("Minimum Sales:",np.min(waiting_time))
print ("StandarDeviation",np.std(waiting_time))

#Boolean Filtering
print ("Waiting time grater than 50 ",waiting_time[waiting_time>50])
print ("Waiting time less than 30",waiting_time[waiting_time<30])
print ("Waiting time between 30 and 50",waiting_time[(waiting_time >= 30) & (waiting_time <= 50)])

#Counting
print ("Count of Waiting time grater than 50 ",[waiting_time>50])
print ("Count of Waiting time less than 30",waiting_time[waiting_time<30])
print ("Count of Waiting time between 30 and 50",waiting_time[(waiting_time >= 30) & (waiting_time <= 50)])

#Position/Index Analysis
print("Count > 50:", np.sum(waiting_time > 50))
print("Count < 30:", np.sum(waiting_time < 30))
print("Percentage above 50:",m)
print("Count < 40:", np.sum(waiting_time < 40))


#Data Modification
waiting_time[waiting_time > 60] = 60
print("Modified waiting time:", waiting_time)  
print("Count < 30:", np.sum(waiting_time < 30))
print("Percentage above 50:",m)
print("Count < 40:", np.sum(waiting_time < 40))







