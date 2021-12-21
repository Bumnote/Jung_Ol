L = list(map(int, input().split()))
L.sort(reverse=True)
for i in range(len(L)):
    print(L[i], end=" ")
