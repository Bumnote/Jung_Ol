first = set(list(map(int, input().split())))
second = set(list(map(int, input().split())))

# set의 차집합 활용
answer = list(first - second)
answer.sort()

for i in answer:
    print(i, end=" ")
