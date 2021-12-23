def solution(a, b, c):
    answer = a if a > b else b  # 삼항 연산자
    answer = answer if answer > c else c
    print(answer)


a, b, c = map(int, input().split())
solution(a, b, c)
