from fastapi import APIRouter
from app.schemas.status import HealthResponse, StatusResponse
from app.services.monitoring_service import MonitorService

router = APIRouter(tags=["Monitoring"])

monitor_service = MonitorService()

@router.get("/health", response_model=HealthResponse)
async def get_health():
    return await monitor_service.get_health()

@router.get("/status", response_model=StatusResponse)
async def get_status():
    return await monitor_service.get_status()