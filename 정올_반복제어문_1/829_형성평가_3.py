Sum = 0
cnt = 0
while True:
    n = int(input())
    if n < 0 or n > 100:
        break

    Sum += n
    cnt += 1

print("sum : %d\navg : %.1f" % (Sum, (Sum / cnt)))
