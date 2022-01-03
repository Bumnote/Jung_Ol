class Information:
    name = ""
    height = 0
    weight = 0.0

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


person = []

for _ in range(5):
    name, height, weight = input().split()
    p = Information(name, int(height), float(weight))
    person.append(p)
# 이름만을 뽑아서 새로운 리스트에 저장
print("name")
name = []
for i in person:
    name.append(i.name)
# 이름 리스트를 오름차순으로 정렬
name.sort()
# 출력
for i in name:
    for j in person:
        if j.name == i:
            print("%s %d %.1f" % (j.name, j.height, j.weight))
print()
# 몸무게만을 뽑아서 새로운 리스트에 저장
print("weight")
weight = []
for i in person:
    weight.append(i.weight)
# 몸무게 리스트를 오름차순으로 정렬
weight.sort(reverse=True)
# 출력
for i in weight:
    for j in person:
        if j.weight == i:
            print("%s %d %.1f" % (j.name, j.height, j.weight))
