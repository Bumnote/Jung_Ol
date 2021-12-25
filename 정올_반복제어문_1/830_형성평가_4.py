cnt = 0
while True:
    n = int(input())
    if n == 0:
        break

    if n % 3 != 0 and n % 5 != 0:
        cnt += 1

print(cnt)
