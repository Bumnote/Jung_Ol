class solution:
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade


name, school, grade = input().split()
student = solution(name, school, grade)
print("Name :", student.name)
print("School :", student.school)
print("Grade :", student.grade)
