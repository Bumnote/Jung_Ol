n = int(input())

star = 1
change = 0
for _ in range(2 * n - 1):
    if change == 0:
        print("*" * star)
        star += 1
        if star == n + 1:
            star -= 1
            change = 1
    else:
        star -= 1
        print("*" * star)
