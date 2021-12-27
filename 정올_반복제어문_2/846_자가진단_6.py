three = 0
five = 0

arr = list(map(int, input().split()))

for i in arr:
    if i % 3 == 0:
        three += 1
    if i % 5 == 0:
        five += 1

print("Multiples of 3 : %d" % (three))
print("Multiples of 5 : %d" % (five))
