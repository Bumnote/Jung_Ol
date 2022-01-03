person = []
for _ in range(3):
    name, tel, addr = input().split()
    p = [name, tel, addr]
    person.append(p)

name = []
for i in person:
    name.append(i[0])
# 이름 순으로 오름차순 정렬
name.sort()
# 가장 빠른 이름과 같다면 그 리스트에 있는 정보 출력
for i in person:
    if name[0] == i[0]:
        print("name :", i[0])
        print("tel :", i[1])
        print("addr :", i[2])
        break
