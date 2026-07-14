from app.services.health_service import HealthService
from app.services.info_service import InfoService


def get_health_service() -> HealthService:
    return HealthService()


def get_info_service() -> InfoService:
    return InfoService()