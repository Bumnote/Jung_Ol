s = input()
Words = list(s.split())
length = len(s)
Word_len = 0
for i in Words:
    if Word_len < len(i):
        Word_len = len(i)

arr = []
for i in Words:
    if len(i) == Word_len:
        arr.append(i)

print(length)
for i in arr:
    print(i, end=" ")
