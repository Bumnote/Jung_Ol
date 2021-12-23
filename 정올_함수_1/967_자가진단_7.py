def solution(n1, n2):
    if n1 > n2:
        n1 //= 2
        n2 *= 2
        print(n1, n2)
    else:
        n2 //= 2
        n1 *= 2
        print(n1, n2)


n1, n2 = map(int, input().split())
solution(n1, n2)
