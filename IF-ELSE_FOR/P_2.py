for i in range (1,51):
    if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5 (i.e., 15)
        print ("FizzBuzz")
    elif(i%3 == 0):
        print ("Fizz")
    elif(i%5 == 0):
        print ("Buzz")
    else:
        print (i)