#number pattern 

n = 5

for i in range(n):
    for j in range(0,n-i):
        print("", end=" ")
    for j in range(0,i+1):
        print(j+1, end=" ")
    for k in range(i, 0,-1):
        print(k, end=" ")
       
    print()