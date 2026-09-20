import os
import requests

T2_URL = os.getenv("T2_URL")

# Fetch student from Neha's microservice
def get_student(student_id: str):
    response = requests.get(f"{T2_URL}/student/{student_id}", timeout=15)
    response.raise_for_status()
    return response.json()