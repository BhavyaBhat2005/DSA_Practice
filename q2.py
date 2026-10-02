n = int(input("enter the number of elements:"))

arr = []

for i in range(n):
    num = int(input(f"enter element {i + 1}:"))
    arr.append(num)

unique_arr = list(set(arr))
unique_arr.sort()

if len(unique_arr) < 2:
    print("Please enter at least two different elements")

else:
    print("largest element:",unique_arr[-1])
    print("second largest element:",unique_arr[-2])
    print("smallest element:",unique_arr[0])
    print("second smallest element:",unique_arr[1])