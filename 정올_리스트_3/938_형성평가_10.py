arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
Sum = 0
Sero_1 = 0
Sero_2 = 0
for y in range(len(arr)):
    Garo = 0
    for x in range(len(arr[y])):
        Sum += arr[y][x]
        Garo += arr[y][x]
    Sero_1 += arr[y][0]
    Sero_2 += arr[y][1]
    print(Garo // 2, end=" ")

print("\n%d %d\n%d" % (Sero_1 // 4, Sero_2 // 4, Sum // 8))
