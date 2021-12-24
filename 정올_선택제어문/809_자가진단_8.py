a, b, c = map(int, input().split())

answer = a if a < b else b
answer = answer if answer < c else c

print(answer)
