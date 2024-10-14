def merge_arrays(arr1,arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
        
    while j < len(arr1):
        result.append(arr1[j])
        j += 1
        
    print(result)
    
merge_arrays([4,5,9,11,15], [1,7,10,19,25])