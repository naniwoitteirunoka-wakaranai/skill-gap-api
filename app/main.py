from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.students import router as students_router
from app.routers.companies import router as companies_router
from app.routers.skill_gap import router as gap_router

app = FastAPI(title="Skill Gap API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students_router)
app.include_router(companies_router)
app.include_router(gap_router)


@app.get("/health")
def health():
    return {"status": "ok"}