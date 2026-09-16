def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
      

result = largest_number([25, 10, 45, 32, 18, 50, 7])
print(result)