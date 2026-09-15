def larger (a,b):
    if a > b:
        return a
    elif a == b:
        return ("Both numbers are equal")
    else:
        return b
    
result = larger(5,10)
print(result)