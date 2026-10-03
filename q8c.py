#diamond pattern

n = 11
mid=n//2

for i in range(n):
    for j in range(n):
        if i+j==mid or j-i==mid or i-j==mid or i+j ==3*mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()