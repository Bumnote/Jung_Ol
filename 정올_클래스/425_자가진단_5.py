class Information:
    # 필드 멤버
    name = ""
    height = 0.0

    # 생성자 
    def __init__(self, name, height):
        self.name = name
        self.height = height

arr = []
for _ in range(5):
    name, height = input().split()
    p = Information(name, height)
    arr.append(p)

Min = arr[0].height
index = 0
for i in arr:
    if Min > i.height:
        Min = i.height
        index = arr.index(i)

print(arr[index].name, arr[index].height)
