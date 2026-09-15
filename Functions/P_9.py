def factorial (n):
    f=1
    for i in range(1,n+1):
        f =f * i
    return f    

result = factorial(5)
print("The factorial of 5 is:", result)