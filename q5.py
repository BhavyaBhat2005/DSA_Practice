#Reverse the Array: Write a program to accept N integers into an array and display the elements in reverse order without changing the original array. 


n = int(input("Enter number of elements"))

arr = []

for i in range(n):
    num = int(input("enter element"))
    arr.append(num)

print("original error", arr)
print("array in reverse order", arr[::-1])