from statistics import mean

from students import get_students
from utils.helpers import highest_score, lowest_score

students = get_students()

print("Student Scores")
print("-" * 20)

for student in students:
    print(student["name"], "-", student["score"])

print()

try:
    top_student = highest_score(students)
    low_student = lowest_score(students)

    average = mean(student["score"] for student in students)

    print("Highest Score")
    print(top_student["name"], "-", top_student["score"])

    print()

    print("Lowest Score")
    print(low_student["name"], "-", low_student["score"])

    print()

    print("Average Score")
    print(f"{average:.2f}")

except ValueError as error:
    print(error)
