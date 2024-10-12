def right_rotate(arr, d):
    n = len(arr)
    d = d % n
    temp = [0] * n
    for i in range(n):
        if i < d:
            temp[i] = arr[n - d + i]
        else:
            temp[i] = arr[i-d]
    for i in range(n):
        arr[i] = temp[i]
        
arr = [1,2,3,4,5]
d = 2
right_rotate(arr, d)
print(arr)