from app.api.schemas.info import InfoResponse
from app.services.base_service import BaseService


class InfoService(BaseService):
    """
    Service responsible for application information.
    """

    def get_info(self) -> InfoResponse:

        self.logger.info("Application information requested.")

        return InfoResponse(
            application=self.settings.APP_NAME,
            version=self.settings.APP_VERSION,
            environment=self.settings.ENVIRONMENT,
            aws_region=self.settings.AWS_REGION,
        )