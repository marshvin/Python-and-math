import numpy as np
import matplotlib.pyplot as plt

def quad_complexity(items):
    count = 0
    for item in items:
        count = count + 1
        for item2 in items:
            print(item, " " ,item)
            
    print("Number of iterations:",len(items))            
quad_complexity([2,3,4,5,67,89,23,9,30,56,77,78,209,232,989,55,32,3,34,1,49,2300])

