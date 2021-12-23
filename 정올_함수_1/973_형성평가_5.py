def solution(L):
    answer = []
    for _ in range(4):
        answer.append([0, 0, 0, 0])
    for y in range(3):
        for x in range(3):
            answer[y][x] = L[y][x]
            answer[y][3] += L[y][x]
            answer[3][x] += L[y][x]
            answer[3][3] += L[y][x]
    # print
    for y in range(4):
        for x in range(4):
            print(answer[y][x], end=" ")
        print()


L = []
for _ in range(3):
    student = list(map(int, input().split()))
    L.append(student)
solution(L)
