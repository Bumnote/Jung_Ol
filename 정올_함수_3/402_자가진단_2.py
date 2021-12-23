def solution(n):
    if n == 0:
        return

    print(n, end=" ")
    return solution(n - 1)


n = int(input())
solution(n)
