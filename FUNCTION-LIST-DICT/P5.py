def even_numbers (numbers):
    even = []
    for num in numbers:
        if num %2==0:
            even.append(num)
    return even

result = even_numbers([10, 15, 22, 33, 40, 51])
print(result)