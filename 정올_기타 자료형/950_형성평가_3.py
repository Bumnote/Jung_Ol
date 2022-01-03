dict = {}

Car = list(input().split())
for i in range(len(Car)):
    if Car[i] in dict:
        dict[Car[i]] += 1
    else:
        dict[Car[i]] = 1

# key 값을 알파벳 순으로 정렬 --> 오름차순
answer = sorted(dict)
for i in answer:
    print(i, end=" ")
print()
print(len(answer))
