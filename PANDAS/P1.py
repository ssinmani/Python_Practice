import pandas as pd 
data = {
    "Patient": ["P101", "P102", "P103", "P104", "P105"],
    "Age": [45, 32, 67, 28, 54],
    "Department": ["Cardiology", "Neurology", "Cardiology",
                   "Emergency", "Neurology"],
    "Waiting_Time": [32, 45, 63, 29, 55]
}

df = pd.DataFrame(data)

print ("Number of rows ",df.shape[0])
print ("Number of column",df.shape[1])
print ("Column Names",df.columns)
print ("Data Types",df.dtypes)
print ("Average Age",df["Age"].mean())
print ("Maximum Waiting Time ",df["Waiting_Time"].max())