n = int(input())
L = [i for i in range(1, 16) if i % n == 0]  # list comprehension

print(L)
