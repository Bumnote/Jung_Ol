def solution(temp, answer):
    if temp == 0:
        print(answer)
        return
    if temp % 10 != 0:
        answer *= (temp % 10)
        return solution(temp // 10, answer)
    else:
        return solution(temp // 10, answer)


a, b, c = map(int, input().split())
temp = a * b * c
answer = 1
solution(temp, answer)
