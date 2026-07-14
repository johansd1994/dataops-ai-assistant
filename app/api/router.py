from fastapi import APIRouter

from app.api.routers.health import router as health_router
from app.api.routers.info import router as info_router
from app.api.routers.chat import router as chat_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    info_router,
    tags=["Information"],
)

api_router.include_router(
    chat_router,
    tags=["Chat"],
)