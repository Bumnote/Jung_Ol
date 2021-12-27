n = int(input())

for y in range(n):
    for x in range(n - y - 1):
        print(" ", end=" ")

    for w in range(1, y + 2):
        print(w, end=" ")
    print()