def solution(n, answer):
    if n == 0:
        print(answer)
        return 0
    answer += n
    return solution(n - 1, answer)


n = int(input())
answer = 0
solution(n, answer)
