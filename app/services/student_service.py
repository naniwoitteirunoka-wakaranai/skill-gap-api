import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "mock" / "students.json"


def get_students():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def get_student(student_id):
    students = get_students()

    for student in students:
        if student["student_id"] == student_id:
            return student

    return None