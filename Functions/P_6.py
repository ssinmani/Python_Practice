def grade (marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80 and marks < 90:
        return "B"
    elif marks >= 70 and marks < 80:
        return "C"
    elif marks >= 60 and marks < 70 :
        return "D"
    else:
        return "F"     
result = grade(45)
print(result)