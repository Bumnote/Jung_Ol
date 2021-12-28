while True:
    s = list(input().strip())
    if s == list("END"):
        break
    s.reverse()
    print("".join(s))
