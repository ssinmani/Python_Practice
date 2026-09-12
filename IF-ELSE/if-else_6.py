a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
if a>b :
    print ("larger number is :" ,a)
elif a==b: # we cannot put exit as its a function is not appropriate to use as exit() is for ending the program, not for handling a normal condition.
     print ("Both the numbers are equal")
else : 
    print ("larger number is :" ,b)
