grade = list(map(int, input().split()))

avg = sum(grade) / len(grade)
print("avg : %.1f" % avg)

if avg >= 80.0:
    print("pass")
else:
    print("fail")
