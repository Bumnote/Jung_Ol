n1, n2 = map(int, input().split())

L = [n1, n2]
while len(L) != 10:
    L.append((L[-2] + L[-1]) % 10)

for i in L:
    print(i, end=" ")
