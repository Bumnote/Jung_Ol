Sum = 0
cnt = 0
while True:
    n = int(input())
    Sum += n
    cnt += 1
    if n >= 100:
        break

print(Sum)
print("%.1f" % (Sum / cnt))
