def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
array = [2,1,7,5,0]
print("Before selection sort: ",array)
selection_sort(array)
print("After selection sort: ",array)