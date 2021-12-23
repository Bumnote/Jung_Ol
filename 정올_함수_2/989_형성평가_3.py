def solution(arr):
    answer = 0
    for i in arr:
        if i < 0:
            i = -i
        answer += i
    print(answer)


arr = list(map(int, input().split()))
solution(arr)
