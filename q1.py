#Write a program to accept N integers into an array and calculate and display the sum of all the elements.

n = int(input("enter number"))
arr = []

for i in range(n):
    num = int(input("enter element"))
    arr.append(num)

total = 0

for num in arr:
    total += num

print("sum=", total)