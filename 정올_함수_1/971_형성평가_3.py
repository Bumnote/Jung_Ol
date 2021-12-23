def solution(n):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(y * x, end=" ")
        print()


n = int(input())
solution(n)
