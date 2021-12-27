n = int(input())
ch = 65
for y in range(n, 0, -1):
    for x in range(y):
        print("%c" % ch, end="")
        ch += 1
        if ch == 91:
            ch = 65
    print()
