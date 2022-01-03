a_year, b_year = map(int, input().split())
answer = 0

for i in range(a_year, b_year + 1):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        answer += 1

print(answer)
