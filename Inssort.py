#program to show insertion sort in python
import time
import matplotlib.pyplot as plt
# creating a function for insertion  
def insertionSort(arr1):
     
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr1)):
 
        key = arr1[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr1[j] :
                arr1[j+1] = arr1[j]
                j -= 1
        arr1[j+1] = key
            
 #Allowing user to input values of array            
arr1=[]
num= len(arr1)
num=int(input("Number of elements in array:"))
print("Enter elements:")
for i in range(0,num):
   l=int(input())
   arr1.append(l)
print("Array before sorting is:", arr1)  
print("Array after sorting:", insertionSort(arr1)) 
#Showing time complexity
start=time.time()
print("Time taken is :", round(time.time() - start, 4))
# Plot graph of time complexity


