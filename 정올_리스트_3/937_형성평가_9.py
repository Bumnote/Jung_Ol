print("first array")
L_1 = []
for _ in range(2):
    L_1.append(list(map(int, input().split())))

print("second array")
L_2 = []
for _ in range(2):
    L_2.append(list(map(int, input().split())))

for y in range(2):
    for x in range(3):
        print(L_1[y][x] * L_2[y][x], end=" ")
    print()
