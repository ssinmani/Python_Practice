def average_marks(student):
    avg = ({student["math"]} + {student["python"]} + {student["science"]}) / 3
    return avg

result = average_marks({
    "name": "Manisha",
    "math": 85,
    "python": 90,
    "science": 88
})
print(f"Average Marks: {result}")