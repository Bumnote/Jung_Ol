n = int(input())
dict = {}
for _ in range(n):
    a, b = input().split()
    dict[a] = b

s = input()
if s in dict:
    print(dict[s])
