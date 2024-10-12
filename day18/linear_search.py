def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i+1
    return -1

arr = [12,32,34,32,12,3,78]
t = 333
result = linear_search(arr,t)
print(f"{t} is present at {result} position!" if result >= 0 else f"{t} is not present in the array!")