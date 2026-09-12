a = int(input("Enter the marks: "))
if (a >= 90 and a<=100):
    print ("Grade is A")
elif (a >= 80 and a<= 89):
    print ("Grade is B")
elif (a >= 70 and a<= 79):
     print ("Grade is C")
elif (a >= 60 and a<= 69):
     print ("Grade is D")
else : # else cannot have condition (if non of the condition are true then thsi will print so do not give condition)
     print ("Grade is F")