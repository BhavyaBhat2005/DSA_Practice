s = input("enter a string")
sub = input("enter a substring")

count = 0
pos = 0

while True:
    pos = s.find(sub,pos)

    if pos == -1:
        break 

    print("found at position",pos)
    count +=1
    pos += 1

print("total occurrences",count)