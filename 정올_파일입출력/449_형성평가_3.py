a, b, c = input().split()

if c == '+':
    print("%s %s %s = %d" % (a, c, b, int(a) + int(b)))
elif c == '-':
    print("%s %s %s = %d" % (a, c, b, int(a) - int(b)))
elif c == '*':
    print("%s %s %s = %d" % (a, c, b, int(a) * int(b)))
elif c == '/':
    print("%s %s %s = %d" % (a, c, b, int(a) // int(b)))
elif c == '%':
    print("%s %s %s = %d" % (a, c, b, int(a) % int(b)))
