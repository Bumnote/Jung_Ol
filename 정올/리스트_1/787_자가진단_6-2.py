L_odd = []
L_even = []
for i in range(6):
    s = input("Element? ")
    if i % 2 == 0:
        L_odd.append(s)
    else:
        L_even.append(s)
answer = L_odd + L_even
print(answer)
