L = ['J', 'U', 'N', 'G', 'O', 'L']
ch = input()
cnt = 0

for i in range(len(L)):
    if L[i] == ch:
        print(i)
        break
    cnt += 1
if cnt == len(L):
    print("none")
