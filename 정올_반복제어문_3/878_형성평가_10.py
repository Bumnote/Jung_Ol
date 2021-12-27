n = int(input())
num = 1
for y in range(n):
    for x in range(n):
        print(num, end=" ")
        num += 2
        if num > 10:
            num = 1
    print()
