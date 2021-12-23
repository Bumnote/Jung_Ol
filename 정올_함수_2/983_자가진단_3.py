def solution_1(n1, n2):
    answer = n1 if abs(n1) > abs(n2) else n2
    print(answer)


def solution_2(f1, f2):
    answer = f1 if abs(f1) < abs(f2) else f2
    print(answer)


n1, n2 = map(int, input().split())
solution_1(n1, n2)

f1, f2 = map(float, input().split())
solution_2(f1, f2)
