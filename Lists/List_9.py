numbers = [10, 15, 22, 33, 40, 51, 60]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("The largest number in the list is:", largest)