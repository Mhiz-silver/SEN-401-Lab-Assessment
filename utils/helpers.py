from statistics import mean


def highest_score(student_list):
    if not student_list:
        raise ValueError("Student list is empty.")

    highest = student_list[0]

    for student in student_list:
        if student["score"] > highest["score"]:
            highest = student

    return highest


def lowest_score(student_list):
    if not student_list:
        raise ValueError("Student list is empty.")

    lowest = student_list[0]

    for student in student_list:
        if student["score"] < lowest["score"]:
            lowest = student

    return lowest


def average_score(student_list):
    if not student_list:
        raise ValueError("Student list is empty.")

    scores = []

    for student in student_list:
        scores.append(student["score"])

    return mean(scores)
