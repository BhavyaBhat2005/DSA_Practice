#Move Zeros to the End: Write a program to accept N integers into an array and rearrange the elements so that all 0 values are moved to the end while maintaining the relative order of the non-zero elements.


n = int(input("Enter number of elements"))

arr = []

for i in range(n):
    num = int(input("enter element"))
    arr.append(num)

result = []

for num in arr:
    if num != 0:
        result.append(num)

for num in arr:
    if num == 0:
        result.append(num)

print("original array:", arr)
print("array in moving zeros", result)