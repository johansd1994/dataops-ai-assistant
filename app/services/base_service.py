from app.core.logger import app_logger
from app.core.settings import settings


class BaseService:
    """
    Base class for all application services.
    """

    def __init__(self) -> None:
        self.logger = app_logger
        self.settings = settings