n = int(input())
grade = []

for _ in range(n):
    arr = list(map(int, input().split()))
    grade.append((round(sum(arr) / 3, 1)))

grade.sort(reverse=True)
for i in grade:
    print(i)
