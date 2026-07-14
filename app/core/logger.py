"""
Enterprise Logger

Centralized logging for the entire application.
"""

import sys
from pathlib import Path

from loguru import logger

from app.core.settings import settings


LOG_PATH = Path("logs")
LOG_PATH.mkdir(exist_ok=True)


class LoggerManager:
    """
    Configures the application logger.
    """

    @staticmethod
    def configure() -> None:

        logger.remove()

        # Console Logger

        logger.add(
            sys.stdout,
            level=settings.LOG_LEVEL,
            colorize=True,
            enqueue=True,
            backtrace=True,
            diagnose=True,
            format=(
                "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:"
                "<cyan>{function}</cyan>:"
                "<cyan>{line}</cyan> | "
                "<level>{message}</level>"
            ),
        )

        # File Logger

        logger.add(
            LOG_PATH / "application.log",
            level=settings.LOG_LEVEL,
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            enqueue=True,
            serialize=False,
        )

        # JSON Logger

        logger.add(
            LOG_PATH / "application.json",
            level=settings.LOG_LEVEL,
            serialize=True,
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            enqueue=True,
        )


LoggerManager.configure()

from typing import Any


class ApplicationLogger:
    """
    Wrapper del logger de Loguru.

    El resto de la aplicación nunca debe importar Loguru directamente.
    """

    def trace(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).trace(message)

    def debug(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).debug(message)

    def info(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).info(message)

    def success(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).success(message)

    def warning(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).warning(message)

    def error(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).error(message)

    def critical(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).critical(message)

    def exception(self, message: str, **kwargs: Any) -> None:
        logger.bind(**kwargs).exception(message)

app_logger = ApplicationLogger()