import pandas as pd 
data = {
    "Patient": ["P101", "P102", "P103", "P104", "P105"],
    "Age": [45, 32, 67, 28, 54],
    "Department": ["Cardiology", "Neurology", "Cardiology",
                   "Emergency", "Neurology"],
    "Waiting_Time": [32, 45, 63, 29, 55]
}

df = pd.DataFrame(data)
print ("Three Columns", df [["Patient","Department","Waiting_Time"]])
