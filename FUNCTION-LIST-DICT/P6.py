def employee_salary(employee):
    return (f"Salary: {employee['salary']}")


result = employee_salary( {
    "name": "Manisha",
    "department": "IT",
    "salary": 50000,
    "experience": 3
} )
print(result)