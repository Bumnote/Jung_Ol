L = list(map(int, input().split()))

Sum_even = 0
Sum_odd = 0
for i in range(len(L)):
    if i % 2 == 1:
        Sum_even += L[i]
    else:
        Sum_odd += L[i]
print("sum : %d" % Sum_even)
print("avg : %.1f" % (Sum_odd / 5))
