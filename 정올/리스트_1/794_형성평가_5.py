L = list(input().split())
answer = [L[i] for i in range(len(L)) if (i + 1) % 3 == 0]
# list comprehension.
print(answer)
