s1, s2, n = input().split()

s1 = s1 + s2
print(s1)

if int(n) >= len(s2):
    arr = list(s1)
    for i in range(int(n)):
        print(arr[i], end="")
else:
    arr = list(s2)
    for i in range(int(n)):
        arr[i] = s1[i]

    for i in arr:
        print(i, end="")
