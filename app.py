from students import get_students
from utils.helpers import highest_score, lowest_score

students = get_students()

print("Student Scores")
print("-" * 20)

for student in students:
    print(student["name"], "-", student["score"])

print()

top_student = highest_score(students)
low_student = lowest_score(students)

print("Highest Score")
print(top_student["name"], "-", top_student["score"])

print()

print("Lowest Score")
print(low_student["name"], "-", low_student["score"])
