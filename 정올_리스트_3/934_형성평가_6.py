L = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
Sum = 0
for y in range(len(L)):
    for x in range(len(L[0])):
        Sum += L[y][x]
        print(L[y][x], end=" ")
    print()
print(Sum)
