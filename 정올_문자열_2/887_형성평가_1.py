arr = input()

answer = arr.split(' (space) ')
answer.reverse()

for i in answer:
    print(i.strip())
