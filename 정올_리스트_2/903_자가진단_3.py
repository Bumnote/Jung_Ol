L = []
for _ in range(10):
    s = input().strip()  # strip() 공백 제거
    L.append(s)

str = input()
for i in L:
    if i[-1] == str:
        print(i)
