def solution(n):
    for y in range(n):
        for x in range(1, n + 1):
            print("%d" % (n * y + x), end=" ")
        print()


n = int(input())
solution(n)
