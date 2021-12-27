c1, c2 = input().split()

if ord(c1) > ord(c2):
    for i in range(ord(c1), ord(c2) - 1, -1):
        print("%c" % i, end=" ")
else:
    for i in range(ord(c1), ord(c2) + 1):
        print("%c" % i, end=" ")
