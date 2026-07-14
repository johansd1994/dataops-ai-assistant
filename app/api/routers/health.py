from fastapi import APIRouter, Depends

from app.api.dependencies import get_health_service
from app.api.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
)
async def health_check(
    service: HealthService = Depends(get_health_service),
) -> HealthResponse:

    return service.get_health()