n = int(input())

arr = [[1] * i for i in range(n, 0, -1)]

for y in range(n - 3, -1, -1):
    for x in range(len(arr[y])):
        if x != 0 and x + y < n - 1:
            arr[y][x] = arr[y + 1][x - 1] + arr[y + 1][x]

for y in arr:
    for x in y:
        print(x, end=" ")
    print()
