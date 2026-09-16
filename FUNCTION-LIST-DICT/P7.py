def student_details (student): # student is a list of dictionaries
    highest_marks =0 # variable to store the highest marks we have found so far.
    top_student = "" #It will store the name of the student with the highest marks.
    for s in student:   #Go through every item in the student list, one at a time.
        if s["marks"] > highest_marks: #s["marks"] This is dictionary access.
            highest_marks = s["marks"]
            top_student = s["name"]
    return(f"Top Student: {top_student} with Marks: {highest_marks}")

#s is simply a temporary variable.During each loop, s represents one dictionary.

result =student_details([
    {"name": "John", "marks": 85},
    {"name": "Manisha", "marks": 92},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 88}
    ])
print (result)