arr = [12,344,32,12,32,14,1,7,5,-99]
min = 9999
max = 0
for i in arr:
    if i > max:
        max = i
    if min > i:
        min = i
        
print(f"Min: {min}\nMax: {max}")