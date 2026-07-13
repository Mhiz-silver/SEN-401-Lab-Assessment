def highest_score(student_list):

    highest = student_list[0]

    for student in student_list:
        if student["score"] > highest["score"]:
            highest = student

    return highest


def lowest_score(student_list):
    lowest = student_list[0]

    for student in student_list:
        if student["score"] < lowest["score"]:
            lowest = student

    return lowest
