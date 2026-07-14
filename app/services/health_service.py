from app.api.schemas.health import HealthResponse
from app.services.base_service import BaseService


class HealthService(BaseService):
    """
    Service responsible for application health operations.
    """

    def get_health(self) -> HealthResponse:

        self.logger.info("Health check requested.")

        return HealthResponse(
            status="healthy",
            application=self.settings.APP_NAME,
            version=self.settings.APP_VERSION,
        )