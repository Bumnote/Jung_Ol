check = 0
number = list(map(int, input().split()))
for i in number:
    if i == 0:
        break
    if i % 3 == 0 and i % 5 == 0:
        check += 1
        print(i, end=" ")

if check != 0:
    print("\n%d" % check)
else:
    print(check)
