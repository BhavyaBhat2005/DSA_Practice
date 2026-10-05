s = input("enter a sentence")

words = s.split()

for word in words:
    print(word[::-1],end="")