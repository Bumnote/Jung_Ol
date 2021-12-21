L = ["flower", "rose", "lily", "daffodil", "azalea"]

s = input()
cnt = 0
for i in L:
    if i[1] == s or i[2] == s:
        cnt += 1
        print(i)
print(cnt)
