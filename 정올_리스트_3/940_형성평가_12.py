arr = []
for _ in range(3):
    arr.append(list(input().split()))

for y in range(len(arr)):
    for x in range(len(arr[y])):
        print("%c" % (ord(arr[y][x]) + 32), end=" ")
    print()
