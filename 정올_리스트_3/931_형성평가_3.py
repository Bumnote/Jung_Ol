arr = list(map(int, input().split()))
cnt = [0] * 6

for i in arr:
    cnt[i - 1] += 1

for i in range(len(cnt)):
    print("%d : %d" % (i + 1, cnt[i]))
