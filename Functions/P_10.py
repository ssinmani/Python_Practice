def calculator (a,b, opeartor):
    if opeartor == "+":
        return a + b
    elif opeartor == "-":
        return a - b
    elif opeartor == "*":
        return a * b
    elif opeartor == "/":
        return a / b
    else:
        return "Invalid operator"

result = calculator(5,10,"+")
print("The result of calculation is:", result)