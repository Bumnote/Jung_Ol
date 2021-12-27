arr = []
for _ in range(3):
    arr.append(input().strip())

temp = arr.copy()
arr.sort()

if temp == arr:
    print("YES")
else:
    print("NO")
