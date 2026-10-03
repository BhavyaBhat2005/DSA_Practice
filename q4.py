# Search an Element: Write a program to accept N integers into an array and search for a given number. Display an appropriate message indicating whether the number is present in the array or not and also display its position.


n = int(input("Enter number of elements"))

arr = []

for i in range(n):
    num = int(input("enter element"))
    arr.append(num)

search = int(input("enter the number to search"))

if search in arr:
    position = arr.index(search) + 1
    print("number is present in the array")
    print("position",position)

else:
   print("Number not in array")
