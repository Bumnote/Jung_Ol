from math import sqrt, floor, ceil

def solution(f1, f2):
    cnt = 0
    if f1 > f2:
        f1, f2 = f2, f1
    f1 = ceil(sqrt(f1))
    f2 = floor(sqrt(f2))
    for i in range(f1, f2 + 1):
        cnt += 1
    print(cnt)


f1, f2 = map(float, input().split())
solution(f1, f2)
