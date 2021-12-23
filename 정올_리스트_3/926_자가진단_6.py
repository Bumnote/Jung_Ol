print("first array")

arr_1 = []
for _ in range(2):
    arr_1.append(list(map(int, input().split())))

print("second array")

arr_2 = []
for _ in range(2):
    arr_2.append(list(map(int, input().split())))

for y in range(2):
    for x in range(4):
        print(arr_1[y][x] * arr_2[y][x], end=" ")
    print()
