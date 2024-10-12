def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
            
    return -1

arr = [12,23,29,45,47,67,68,69,70]
target = 70
result = binary_search(arr, target)

print(f"Target element is found at {result}!" if result>=0 else f"Element not found!")