L = []

while True:
    n = int(input())
    if n == -1:
        break
    L.append(n)

if len(L) < 3:
    for i in L:
        print(i, end=" ")
else:
    answer = L[len(L) - 3:]
    for i in answer:
        print(i, end=" ")
