def remove_element(arr, target):
    i = -1
    for j in range(len(arr)):
        if arr[j] != target:
            i+=1
            arr[i] = arr[j]
    print(i)
    print(arr)
    
remove_element([3,2,2,3],3)