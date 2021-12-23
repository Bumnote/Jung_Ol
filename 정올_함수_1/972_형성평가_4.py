def solution(a, b):
    if a < b:
        a, b = b, a
    answer = a ** 2 - b ** 2
    print(answer)


a, b = map(int, input().split())
solution(a, b)
