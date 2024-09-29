# Data Overlap
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 

with open("file1.txt", "r") as f1:
    list1 = f1.readlines()
with open("file2.txt", "r") as f2:
    list2 = f2.readlines()
    
result = [int(number) for number in list1 if number in list2]  #list comprehension
print(result)