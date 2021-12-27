n = int(input())
num = 1
for y in range(n):
    for t in range(y):
        print(" ", end=" ")

    for w in range(n - y):
        print(num, end=" ")
        num += 1
    print()
