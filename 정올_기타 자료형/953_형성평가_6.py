dict = {}

person = list(input().split())
for i in person:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

Min = min(dict.values())
for i in dict:
    if dict[i] == Min:
        print(i)
print(Min)
