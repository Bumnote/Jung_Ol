from math import floor, ceil

def solution(L):
    L.sort()
    L[0] = floor(L[0])
    L[-1] = ceil(L[-1])
    L[1] = round(L[1])
    print(L[-1], L[0], L[1])

f1, f2, f3 = map(float, input().split())
L = [f1, f2, f3]
solution(L)
