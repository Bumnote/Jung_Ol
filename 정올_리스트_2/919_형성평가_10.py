L = []
cnt = 0
for _ in range(5):
    L.append(input().strip())

ch = input().strip()
s = input().strip()

for i in L:
    if i.count(ch) != 0 or i.count(s) != 0:
        cnt += 1
        print(i)

if cnt == 0:
    print("none")
