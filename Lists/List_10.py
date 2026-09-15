numbers = [10, -5, 20, 0, -8, 15, -2, 7]
c=0
z=0
y=0
for number in numbers:
    if number > 0 :
        c=c+1
    elif number == 0:
        z=z+1
    elif number < 0:
        y=y+1
print("The number of positive numbers in the list is:", c)
print("The number of negative numbers in the list is:", y)
print("The number of zeros in the list is:", z)