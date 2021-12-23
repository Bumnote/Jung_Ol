L = [[1, 0, 1, 0, 1]]

for _ in range(4):
    L.append([0] * 5)

for y in range(1, len(L)):
    for x in range(len(L[y])):
        if x == 0:
            L[y][x] = L[y - 1][x + 1]
        elif x == 4:
            L[y][x] = L[y - 1][x - 1]
        else:
            L[y][x] = L[y - 1][x - 1] + L[y - 1][x + 1]

for y in L:
    for x in y:
        print(x, end=" ")
    print()
