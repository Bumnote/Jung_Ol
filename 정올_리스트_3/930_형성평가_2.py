Len, n = map(int, input().split())

arr = [False for i in range(Len)]
for i in range(Len):
    if i % n == 0:
        arr[i] = True
print(arr)
