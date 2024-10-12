arr = [45,56,43,23,42]
new_arr= []
for i in range(len(arr) - 1,-1,-1):
    new_arr.append(arr[i])
    
print(new_arr)