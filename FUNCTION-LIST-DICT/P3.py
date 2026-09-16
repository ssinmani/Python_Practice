def student_details(student):
    print("Name: student['name']")
    print(f"Math: {student['math']}")
    print(f"Python: {student['python']}")
    print(f"Science: {student['science']}")

#We use single quotes there simply because the outside string is already using double quotes.
result = student_details({
    "name": "Manisha",
    "math": 85,
    "python": 90,
    "science": 88
})