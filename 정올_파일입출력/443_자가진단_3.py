name = []
score = []

for _ in range(10):
    a, b = input().split()
    name.append(a)
    score.append(int(b))

# 성적을 내림차순으로 정렬 --> 인덱싱이 편하다.
rank = sorted(score, reverse=True)

print("Name", "Score", "Rank")
for i in range(10):
    print("%4s%6d%5d" % (name[i], score[i], rank.index(score[i]) + 1))
