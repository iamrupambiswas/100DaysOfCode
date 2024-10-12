def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, mid-1, target)
    elif arr[mid] < target:
        return binary_search(arr, mid+1, end, target)
    
arr = [12,23,29,45,47,67,68,69,70]
target = 7
start = 0
end = len(arr) - 1
result = binary_search(arr, start, end, target)

print(f"Target element is found at {result}!" if result != -1 else "Element not found!")