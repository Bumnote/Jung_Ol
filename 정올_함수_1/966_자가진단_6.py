def solution(a, s, b):
    if s == "+":
        print("%d %s %d = %d" % (a, s, b, a + b))
    elif s == "-":
        print("%d %s %d = %d" % (a, s, b, a - b))
    elif s == "*":
        print("%d %s %d = %d" % (a, s, b, a * b))
    elif s == "/":
        print("%d %s %d = %d" % (a, s, b, a // b))
    else:
        print(0)


a, s, b = input().split()
a = int(a)
b = int(b)
solution(a, s, b)
