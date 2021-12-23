arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
cnt = 0
for y in range(5):
    sum = 0
    for x in range(4):
        sum += arr[y][x]

    if sum >= 320:
        print("pass")
        cnt += 1
    else:
        print("fail")

print("Successful : %d" % cnt)
