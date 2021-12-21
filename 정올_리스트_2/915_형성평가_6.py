L = list(map(int, input().split()))

print(len(L))

for i in L:
    if i % 2 == 1:
        print(i * 2, end=" ")
    else:
        print(int(i / 2), end=" ")
