def optimized_bubble_sort(arr):
    for i in range(len(arr)):
        isSwap = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwap = True
        if isSwap == False:
            break

# array = [2,1,7,5,0]
array = [1,2,3,4,5]
print("Before bubble sort: ",array)
optimized_bubble_sort(array)
print("After bubble sort: ",array)