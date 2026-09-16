def student_details(students):
    for students in students:
     print(f"Name: {students['name']} , Marks: {students['marks']}")


student_details([
    {"name": "John", "marks": 85},
    {"name": "Manisha", "marks": 92},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 88}
    ])

#students → whole list
#student  → one dictionary