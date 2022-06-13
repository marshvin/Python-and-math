#program to perform a bubble sort given input by user
#function to sort
def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
#allow user to input values  
if __name__ == '__main__':
    data = []
    arr1=[]
num= len(data)
num=int(input("Number of elements in array:"))
print("Enter elements:")
for i in range(0,num):
   l=int(input())
   data.append(l)
print("Array before sorting is:", data)
bubble_sort(data)
print(data)
