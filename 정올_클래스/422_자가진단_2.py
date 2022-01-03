class solution:
    def __init__(self, school, grade):
        self.school = school
        self.grade = grade


school, grade = input().split()
a = solution("Jejuelementary", 6)
b = solution(school, int(grade))

print(a.grade, "grade in", a.school, "School")
print(b.grade, "grade in", b.school, "School")
