n = int(input())
star = 1
blank = 2 * n - 2
for i in range(n):
    print(" " * blank + "*" * star)
    star += 2
    blank -= 2
