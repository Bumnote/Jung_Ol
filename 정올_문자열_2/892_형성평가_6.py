s = input()
if s.isupper():
    print("U")
    print(s)
elif s.islower():
    print("L")
    print(s.upper())
elif s.isdigit():
    print("D")
    print(s)
else:
    print("X")
    print(s.upper())
