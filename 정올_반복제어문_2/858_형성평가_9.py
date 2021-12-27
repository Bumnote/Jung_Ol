n = int(input())

for y in range(1, n + 1):
    for x in range(1, n + 1):
        print("(%d, %d)" % (y, x), end=" ")
    print()
