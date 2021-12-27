n = int(input())

star = n * 2 - 1
change = 0
blank = 0
for i in range(2 * n - 1):
    if change == 0:
        print(" " * blank + "*" * star)
        if star == 1:
            change = 1
            continue
        star -= 2
        blank += 1

    else:
        star += 2
        blank -= 1
        print(" " * blank + "*" * star)
