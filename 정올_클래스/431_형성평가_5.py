class Information:
    name = ""
    a = 0
    b = 0
    c = 0
    total = 0

    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    # total 을 설정해주는 메소드
    def set_total(self, a, b, c):
        self.total = a + b + c


n = int(input())
person = []
for _ in range(n):
    name, a, b, c = input().split()
    p = Information(name, int(a), int(b), int(c))
    p.set_total(p.a, p.b, p.c)
    person.append(p)

total = []
for i in person:
    total.append(i.total)
total.sort(reverse=True)

for i in total:
    for j in person:
        if i == j.total:
            print("%s %d %d %d %d" % (j.name, j.a, j.b, j.c, j.total))
            # 점수가 중복된 경우를 방지하기 위한 작업
            j.total = 0
            break
