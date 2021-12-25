odd = 0
even = 0
while True:
    n = int(input())
    if n == 0:
        break

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("odd : %d\neven : %d" % (odd, even))
