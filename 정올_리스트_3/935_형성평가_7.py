Student = []
for i in range(4):
    Student.append(list(map(int, input(str(i + 1) + "class? ").split())))

for y in range(len(Student)):
    Sum = 0
    for x in range(len(Student[y])):
        Sum += Student[y][x]
    print("%dclass : %d" % (y + 1, Sum))
