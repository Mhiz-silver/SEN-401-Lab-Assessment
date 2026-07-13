"""
students.py

This module stores student records and provides
a function to retrieve the student data.
"""


# List of student records.
# Each student is represented as a dictionary.
STUDENTS = [
    {"name": "Chidi Gloria", "score": 48},
    {"name": "Mohammed Adamu", "score": 51},
    {"name": "Ogechi Chukwuka", "score": 35},
    {"name": "Onyinye Silver", "score": 88},
    {"name": "Ngozi Victory", "score": 74}
]


def get_students():
    """
    Returns the list of student records.

    Returns:
        list: A list containing student dictionaries.
    """
    return STUDENTS.copy()
