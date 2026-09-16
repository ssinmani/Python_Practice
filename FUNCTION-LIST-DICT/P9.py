def employee_details (employees): #employees = the whole list
    for employee in employees:
        if employee["salary"] >50000:
          print (f"Name :{employee["name"]} ,Salary:{employee["salary"]}")


employee_details ([
   {"name" : "Manisha Singh" ,"salary" :45000 },
   {"name" : "Rishu" ,"salary" :450000},
   {"name" : "Tim" ,"salary" :46000 },
   {"name": "John", "salary": 45000},
   {"name": "ManishaS", "salary": 65000},
   {"name": "Rahul", "salary": 55000},
    {"name": "Priya", "salary": 48000}
])

""" employees                    # whole list

employee                     # one dictionary from the list

employee["salary"]           # salary from that dictionary

employee["salary"] > 50000   # check the salary

employee["name"]             # get the name """