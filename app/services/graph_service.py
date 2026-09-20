import os
import requests

GRAPH_URL = os.getenv("GRAPH_URL", "http://localhost:9000")


def analyze(student, job):
    try:
        res = requests.post(
            f"{GRAPH_URL}/run",
            json={"student": student, "job": job},
            timeout=10,
        )

        res.raise_for_status()

        return res.json()

    except Exception:
        student_skills = {s["skill"].lower() for s in student["skills"]}

        matched = []
        gaps = []

        for skill in job["skills"]:
            if skill["skill"].lower() in student_skills:
                matched.append(skill)
            else:
                gaps.append({
                    **skill,
                    "reason": "Missing from student profile"
                })

        score = round(len(matched) / len(job["skills"]) * 100)

        return {
            "matchedSkills": matched,
            "skillGaps": gaps,
            "matchScore": score,
            "summary": {
                "matched": len(matched),
                "missing": len(gaps),
                "preferredMissing": 0,
            },
        }