Words = []
for _ in range(10):
    Words.append(input().strip())

s = input()
answer = []
for i in Words:
    if i.count(s) != 0:
        answer.append(i)

answer.sort()
for i in answer:
    print(i)
