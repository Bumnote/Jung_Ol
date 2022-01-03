arr = list(input().split())
n = int(input())
person = {}

for i in range(len(arr)):
    if arr[i] in person:
        person[arr[i]] += 1
    else:
        person[arr[i]] = 1

for i in person.keys():
    if person[i] == n:
        print(i)
