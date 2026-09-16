def employee_details(employees):
    for employee in employees:
        if (employee["department"] =="IT" and employee["salary"] > 50000 ):
          print(f"Name :{employee['name']} ,Salary:{employee['salary']}")

employee_details ( [
    {"name": "John", "department": "IT", "salary": 45000},
    {"name": "Manisha", "department": "IT", "salary": 65000},
    {"name": "Rahul", "department": "HR", "salary": 55000},
    {"name": "Priya", "department": "IT", "salary": 75000},
    {"name": "Rishu", "department": "HR", "salary": 48000}
])