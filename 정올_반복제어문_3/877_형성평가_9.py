n = int(input())
change = 0
sharp = 1
blank = 0
for i in range(2 * n - 1):
    if change == 0:
        print("# " * sharp)
        sharp += 1
        if sharp == n:
            change = 1
    else:
        print("  " * blank + "# " * sharp)
        sharp -= 1
        blank += 1
