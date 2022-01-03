class Body:
    height = 0
    weight = 0.0

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


person = []
for _ in range(2):
    height, weight = input().split()
    p = Body(int(height), float(weight))
    person.append(p)

height = 0
weight = 0
for i in person:
    height += i.height
    weight += i.weight

answer = Body(height / 2 + 5, weight / 2 - 4.5)
print("height : %dcm" % (answer.height))
print("weight : %.1fkg" % (answer.weight))
