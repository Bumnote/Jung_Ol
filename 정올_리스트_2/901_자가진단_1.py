L = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
a, b = map(int, input().split())

answer = L[a - 1] + L[b - 1]
print("%.1f" % answer)
