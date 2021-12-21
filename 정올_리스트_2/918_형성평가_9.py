L = []
cnt = 0
while True:
    s = input()
    if s == '0':
        break
    cnt += 1
    L.append(s)

print(cnt)
for i in L:
    if i.count("mo") != 0:
        print(i)
