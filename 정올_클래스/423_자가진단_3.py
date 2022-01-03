class solution:
    def __init__(self, name, Korean, English):
        self.name = name
        self.Korean = Korean
        self.English = English


name, korean, english = input().split()
a = solution(name, int(korean), int(english))

name, korean, english = input().split()
b = solution(name, int(korean), int(english))

print("%s %s %s" % (a.name, a.Korean, a.English))
print("%s %s %s" % (b.name, b.Korean, b.English))
print("avg %d %d" % ((a.Korean + b.Korean) / 2, (a.English + b.English) / 2))
