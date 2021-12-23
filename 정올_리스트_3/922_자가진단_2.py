arr = list(input().split())

cnt = [0] * 26
for i in arr:
    cnt[ord(i) - 65] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        print("%c : %d" % (i + 65, cnt[i]))
