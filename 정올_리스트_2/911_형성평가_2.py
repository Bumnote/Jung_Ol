L = list(map(float, input().split()))
Sum = 0
for i in L:
    Sum += i
print("%.1f" % (Sum / len(L)))
