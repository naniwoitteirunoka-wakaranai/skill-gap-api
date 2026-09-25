from fastapi import APIRouter
from app.services.student_service import get_students

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("")
def students():
    return get_students()