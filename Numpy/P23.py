import numpy as np

sales = np.array([
    12000, 15000, 11000, 18000,
    22000, 17000, 14000, 25000,
    21000, 19000, 23000, 27000
])
s= np.mean(sales)

print("Total:",np.sum(sales))
print("Average:",np.mean(sales))
print("Maximum:",np.max(sales))
print("Minimum Sales:",np.min(sales))
print("Index of Maximum Sales:",np.argmax(sales))
print ("StandarDeviation" , np.std(sales))
print ("Sorted Arrays" , np.sort(sales))
print ("Sales value greater than average ",sales[sales>s])
print ("Count the values greater than the average",np.sum(sales>s))
print ("Range:",(np.max(sales)-np.min(sales)))
print ( "Month number that had higher sales",np.argmax(sales)+1)

