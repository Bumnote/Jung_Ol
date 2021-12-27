n = int(input())

star = 1
change = 0
for _ in range(2 * n - 1):
    if change == 0:
        print("*" * star)
        star += 1
        if star == n:
            change = 1
    else:
        print("*" * star)
        star -= 1
