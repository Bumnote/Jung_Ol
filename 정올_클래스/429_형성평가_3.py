class Square:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


x1, y1, x2, y2 = map(int, input().split())
s1 = Square(x1, y1, x2, y2)

x1, y1, x2, y2 = map(int, input().split())
s2 = Square(x1, y1, x2, y2)

x1 = s1.x1 if s1.x1 < s2.x1 else s2.x1
y1 = s1.y1 if s1.y1 < s2.y1 else s2.y1
x2 = s1.x2 if s1.x2 > s2.x2 else s2.x2
y2 = s1.y2 if s1.y2 > s2.y2 else s2.y2

answer = Square(x1, y1, x2, y2)
print(answer.x1, answer.y1, answer.x2, answer.y2)
