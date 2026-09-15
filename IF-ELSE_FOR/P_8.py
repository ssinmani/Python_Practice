c=0
z=0
for i in range(10):
    n = int(input("Enter a number: "))

    if n%2 == 0:
        c=c+1
    else:
        z=z+1  
print("The number of even numbers is:", c)
print("The number of odd numbers is:", z)   
