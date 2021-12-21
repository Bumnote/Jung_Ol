L = list(map(int, input().split()))

Sum = 0
cnt = 0

for i in L:
    if i % 5 == 0:
        cnt += 1
        Sum += i

print("Multiples of 5 : %d" % cnt)
print("sum : %d" % Sum)
print("avg : %.1f" % (Sum / cnt))
