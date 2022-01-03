n = int(input())
person = [tuple(list(input().split())) for _ in range(n)]

for i in range(len(person)):
    if person[i][-1].strip() == 'Platinum' or (person[i][-1] != 'Bronze' and float(person[i][1]) >= 60.0):
        print("[Gosu]", person[i][0].strip())
