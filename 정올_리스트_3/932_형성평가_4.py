arr = list(map(int, input().split()))
cnt = [0] * 11

for i in arr:
    cnt[i // 10] += 1

for i in range(len(cnt) - 1, -1, -1):
    if cnt[i] != 0:
        print("%d : %d person" % (i * 10, cnt[i]))
