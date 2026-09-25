import pandas as pd
import numpy as np 
data ={
    "Patient":["P101","P102","P103","P104","P105"],
    "Age":[45,32,67,28,54],
    "Department":["Cardiology","Neurology","Cardiology","Emergency","Neurology"],
    "Waiting_Time":[32,45,63,29,55]
}

df =pd.DataFrame(data)
print ("All patients whose Age is greater than 40:\n",df[df["Age"]> 40])
print ("All patients whose Waiting_time is less than 40:\n",df[df["Waiting_Time"]< 40])
print ("All patients whose Age is greater than 40 and Waiting _time Greater than 50:\n",(df[(df["Age"]> 40) & (df["Waiting_Time"]> 50)]))
print ("Display all patients whose Department is either Cardiology or Emergency \n",(df[(df["Department"]=="Cardiology")|(df["Department"]=="Emergency")]))
df["Status"] = np.where(df["Waiting_Time"] > 50, "Long", "Normal")
print ("New Column Added ",df["Status"])
df["Waiting_time"]= df["Waiting_Time"] + 5
print ("Modify the exisiting column \n",df)
print ("Delete the Status Column \n",df.drop(["Status","Waiting_time"],axis=1))

df = df.sort_values("Waiting_Time")
print ("Data is",df )

df = df.sort_values("Waiting_Time",ascending=False)
print ("Data is",df )