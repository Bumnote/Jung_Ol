n = int(input())
arr = [100, n]

while arr[-1] > 0:
    arr.append(arr[-2] - arr[-1])

for i in arr:
    print(i, end=" ")
