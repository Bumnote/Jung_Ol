L = list(map(int, input().split()))

Max = -1
Min = 10000
for i in range(len(L)):
    if L[i] < 100 and Max < L[i]:
        Max = L[i]
    if L[i] >= 100 and Min > L[i]:
        Min = L[i]

if Max == -1:
    Max = 100
if Min == 10000:
    Min = 100

print(Max, Min)
