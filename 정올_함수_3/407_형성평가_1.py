def solution(n):
    if n == 0:
        return
    solution(n // 2)
    print(n, end=" ")


n = int(input())
solution(n)
