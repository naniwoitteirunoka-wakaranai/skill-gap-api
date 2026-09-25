from fastapi import APIRouter, HTTPException

from app.models.request import SkillGapRequest
from app.services.student_service import get_student
from app.services.company_service import get_company
from app.services.graph_service import analyze

router = APIRouter(tags=["Skill Gap"])


@router.post("/skill-gap")
def skill_gap(req: SkillGapRequest):
    student = get_student(req.studentId)
    job = get_company(req.company, req.role)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    result = analyze(student, job)

    return {
        "studentId": req.studentId,
        "company": req.company,
        "role": req.role,
        **result,
    }