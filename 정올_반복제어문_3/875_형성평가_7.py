n = int(input())
ch = 65
num = 0
for y in range(n):
    for x in range(n - y):
        print("%c" % ch, end=" ")
        ch += 1
        if ch == 91:
            ch = 65
    for w in range(y):
        print(num, end=" ")
        num += 1
    print()
