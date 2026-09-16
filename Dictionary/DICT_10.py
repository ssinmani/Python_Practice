employee = {
    "name": "Manisha",
    "department": "IT",
    "salary": 50000,
    "experience": 3
}

search_key = input("Enter key: ")

if search_key in employee:
    print(f"{search_key}: {employee[search_key]}")
else:
    print("Key not found.")