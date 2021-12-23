arr = []
for _ in range(5):
    arr.append([1] * 5)

for y in range(5):
    for x in range(5):
        if x != 0 and y != 0:
            arr[y][x] = arr[y][x - 1] + arr[y - 1][x]
        print(arr[y][x], end=" ")
    print()
