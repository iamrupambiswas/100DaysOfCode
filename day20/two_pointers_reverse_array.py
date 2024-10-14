def reverse_array(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while end > start:
        temp = arr[end]
        arr[end] = arr[start]
        arr[start] = temp
        start += 1
        end -= 1
    print(arr)
    
reverse_array([5,9,4,3,2])