n = int(input())

for i in range(0, 26):
    if (i + 1) % n == 0:
        print("%c" % (i + 97), end="")
