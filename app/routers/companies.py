from fastapi import APIRouter
from app.services.company_service import get_companies

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("")
def companies():
    return get_companies()