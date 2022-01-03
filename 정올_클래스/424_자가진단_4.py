class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


x1, y1, x2, y2, x3, y3 = map(int, input().split())
s1 = Circle(x1, y1)
s2 = Circle(x2, y2)
s3 = Circle(x3, y3)

answer = (round((s1.x + s2.x + s3.x) / 3, 1), round((s1.y + s2.y + s3.y) / 3, 1))
print(answer)
