from students import get_students
from utils.helpers import (
    highest_score,
    lowest_score,
    average_score,
    median_score
)

students = get_students()

print("=" * 35)
print("      STUDENT SCORE REPORT")
print("=" * 35)

print(f"{'Name':<15}{'Score':>10}")
print("-" * 25)

for student in students:
    print(f"{student['name']:<15}{student['score']:>10}")

print()

try:
    top_student = highest_score(students)
    low_student = lowest_score(students)
    average = average_score(students)
    median = median_score(students)

    print("=" * 35)
    print("SUMMARY")
    print("=" * 35)
    print(f"Highest Score : {top_student['name']} ({top_student['score']})")
    print(f"Lowest Score  : {low_student['name']} ({low_student['score']})")
    print(f"Average Score : {average:.2f}")
    print(f"Median Score  : {median}")

except ValueError as error:
    print(error)
