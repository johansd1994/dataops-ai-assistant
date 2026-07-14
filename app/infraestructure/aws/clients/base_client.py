from abc import ABC

import boto3

from botocore.config import Config

from app.core.logger import app_logger
from app.core.settings import settings


class BaseAWSClient(ABC):
    """
    Base class for every AWS client.
    """

    def __init__(self) -> None:

        self.logger = app_logger

        self.settings = settings

        self.region = settings.AWS_REGION

        self.session = boto3.Session(
            profile_name=self.settings.AWS_PROFILE,
            region_name=self.settings.AWS_REGION,
        )

        self.config = Config(

            retries={

                "max_attempts": 3,

                "mode": "standard",

            }

        )