def solution(n, cnt):
    if n == 1:
        print(cnt)
        return
    if n % 2 == 0:
        solution(n // 2, cnt + 1)
    else:
        solution(n // 3, cnt + 1)


n = int(input())
cnt = 0
solution(n, cnt)
