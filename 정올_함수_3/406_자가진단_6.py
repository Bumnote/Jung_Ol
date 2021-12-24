def solution(n, answer):
    if n == 0:
        print(answer)
        return
    answer += ((n % 10)**2)
    return solution(n // 10, answer)


n = int(input())
answer = 0
solution(n, answer)
