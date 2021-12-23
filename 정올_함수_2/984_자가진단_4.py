from math import sqrt

def solution(Area):
    answer = sqrt(Area / 3.14)
    print("%.2f" % answer)

Area = int(input())
solution(Area)
