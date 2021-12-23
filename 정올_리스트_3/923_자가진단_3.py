arr = list(map(int, input().split()))
cnt = [0] * 10

for i in arr:
    cnt[i // 10] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        print("%d : %d" % (i, cnt[i]))
