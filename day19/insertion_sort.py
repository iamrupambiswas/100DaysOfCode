def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i-1
        while prev >= 0 and arr[prev] > curr:
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = curr
        
array = [2,1,7,5,0]
print("Before insertion sort: ",array)
insertion_sort(array)
print("After insertion sort: ",array)