def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp                
array = [2,1,7,5,0]
print("Before bubble sort: ",array)
bubble_sort(array)
print("After bubble sort: ",array)
    