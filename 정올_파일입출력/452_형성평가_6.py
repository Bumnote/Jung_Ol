n = int(input())
flag = 0
cnt = n-1
for _ in range(2 * n - 1):
    if flag == 0:
        for i in range(cnt):
            print(" ", end=" ")
        for i in range(2 * (n - cnt) - 1):
            print("*", end=" ")
        cnt -= 1
        if cnt == 0:
            flag = 1
    else:
        for i in range(cnt):
            print(" ", end=" ")
        for i in range(2 * (n - cnt) - 1):
            print("*", end=" ")
        cnt += 1
    print()
