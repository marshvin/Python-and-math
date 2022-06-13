# Python program to find the factorial of a number provided by the user.
import matplotlib.pyplot as plt
import time
#Taking input from the user
start=time.process_time()
num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

#Showing time complexity


print("Time taken is :", round(time.process_time()))


