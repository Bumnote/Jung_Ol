s, x, y = input().split()
arr = list(s)

for i in range(int(y)):
    s = arr[int(x):] + arr[0:int(x)]
    arr = s
    for answer in s:
        print(answer, end="")
    print()
