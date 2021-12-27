a, b = map(int, input().split())
if a > b:
    a, b = b, a

Sum = 0
cnt = 0
for i in range(a, b + 1):
    if i % 3 == 0 or i % 5 == 0:
        Sum += i
        cnt += 1

print("sum : %d\navg : %.1f" % (Sum, Sum / cnt))
