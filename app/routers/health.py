from fastapi import APIRouter
from app.services.health.health import check_health

router = APIRouter()

@router.get("/health")
async def health_check():
    return check_health()