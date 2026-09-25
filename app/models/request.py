from pydantic import BaseModel


class SkillGapRequest(BaseModel):
    studentId: str
    company: str
    role: str