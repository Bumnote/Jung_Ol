def solution(a, b):
    if a > b:
        a, b = b, a
    for y in range(a, b + 1):
        print("== %ddan ==" % y)
        for x in range(1, 10):
            print("%d * %d = %2d" % (y, x, y * x))
        print()


a, b = map(int, input().split())
solution(a, b)
