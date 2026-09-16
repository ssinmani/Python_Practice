def add (numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add([ 10, 20, 30, 40 , 50 ])
print(result)