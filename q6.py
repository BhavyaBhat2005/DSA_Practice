#Remove Duplicate Elements: Write a program to accept N integers into an array and create a new array containing only the unique elements, removing all duplicate values. 


n = int(input("Enter number of elements"))

arr = []

for i in range(n):
    num = int(input("enter element"))
    arr.append(num)

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("original error", arr)
print("array after removing duplicates", unique)