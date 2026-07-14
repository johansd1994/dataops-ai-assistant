from fastapi import APIRouter, Depends

from app.api.dependencies import get_info_service
from app.api.schemas.info import InfoResponse
from app.services.info_service import InfoService

router = APIRouter()


@router.get(
    "/info",
    response_model=InfoResponse,
    summary="Application Information",
)
async def application_info(
    service: InfoService = Depends(get_info_service),
) -> InfoResponse:

    return service.get_info()