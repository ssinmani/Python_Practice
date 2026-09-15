n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))
n5 = int(input("Enter the fifth number: "))
z=0
c=0 
p=0
for i in [n1, n2 ,n3 ,n4 ,n5]:
   if (i > 0):
      c=c+1
   elif (i < 0):
       z=z+1
   else:
        p=p+1
print("The number of positive numbers is: ", c)
print("The number of negative numbers is: ", z) 
print("The number of zero numbers is: ", p)

"""positive = 0
negative = 0
zero = 0

for i in range(5):
    n = int(input("Enter a number: "))

    if n > 0:
        positive = positive + 1
    elif n < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print("The number of positive numbers is:", positive)
print("The number of negative numbers is:", negative)
print("The number of zeros is:", zero)"""