arr = [92,93,43,2,12,65,90,90,78]
largest = float('-inf')
second_largest = float('-inf')

for i in range(0, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest:
        second_largest = arr[i]

print(f"Largest: {largest} \nSecond Largest: {second_largest}")