a, b = map(int, input().split())

if a > b:
    for y in range(1, 10):
        for x in range(a, b - 1, -1):
            print("%d * %d = %2d   " % (x, y, x * y), end="")
        print()
else:
    for y in range(1, 10):
        for x in range(a, b + 1):
            print("%d * %d = %2d   " % (x, y, x * y), end="")
        print()
