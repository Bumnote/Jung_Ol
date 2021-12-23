def solution(f1, f2, f3):
    avg_1 = round((f1 + f2 + f3) / 3)
    avg_2 = round((round(f1) + round(f2) + round(f3)) / 3)
    print("%d\n%d" % (avg_1, avg_2))

f1, f2, f3 = map(float, input().split())
solution(f1, f2, f3)
