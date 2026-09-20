import os
import requests

T2_URL = os.getenv(
    "T2_URL",
    "https://t2-student-competency-kg.onrender.com"
)

# Fetch all students (for dropdown in UI)
def get_students():
    response = requests.get(f"{T2_URL}/students", timeout=15)
    response.raise_for_status()

    students = response.json()

    # If Neha returns a wrapper like {"students":[...]}
    if isinstance(students, dict):
        students = students.get("students", [])

    # UI only needs id + name
    return [
        {
            "student_id": student["studentId"],
            "name": student["studentName"],
        }
        for student in students
    ]


# Fetch one complete student profile
def get_student(student_id: str):
    response = requests.get(f"{T2_URL}/student/{student_id}", timeout=15)
    response.raise_for_status()

    student = response.json()

    # Convert Neha's contract to T4's internal shape.
    student["student_id"] = student.pop("studentId")
    student["name"] = student.pop("studentName")

    for skill in student.get("skills", []):
        skill["skill"] = skill.pop("name")

    return student