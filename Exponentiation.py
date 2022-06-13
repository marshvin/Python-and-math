#Exponentiation O(2^n)
import numpy as np
import matplotlib.pyplot as plt
def exponential_time(number):
    if number <= 1:
        return number
    return (exponential_time(number - 1) + exponential_time(number -2))

for i in range(1, 100):
    print(exponential_time(i))

#checking the execution time 
%timeit exponential_time(i)