largest = 0
for i in range(10):
    n = int(input("Enter a number: "))
    if n >= largest:
        largest = n
print("The largest number is:", largest)


"""largest = int(input("Enter a number: "))

for i in range(9):
    n = int(input("Enter a number: "))

    if n > largest:
        largest = n

print("The largest number is:", largest)"""