import array

arr = array.array('i', [1,2,3,4,5])

# accessing element
print(arr[0])

# add an element
arr.append(6)
print(arr)

# remove an element
arr.remove(3)
print(arr)

# updating element
arr[2] = 2
print(arr)