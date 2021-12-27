n = int(input())
num = 1
ch = 65
for y in range(n):
    # 숫자를 먼저 출력
    for x in range((n - y), 0, -1):
        print(num, end=" ")
        num += 1

    for t in range(y + 1):
        print("%c" % ch, end=" ")
        ch += 1
        # Z를 넘어가면 다시 A 로 초기화
        if ch == 91:
            ch = 65
    print()
