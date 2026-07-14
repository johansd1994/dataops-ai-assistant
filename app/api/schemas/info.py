from pydantic import BaseModel


class InfoResponse(BaseModel):
    application: str
    version: str
    environment: str
    aws_region: str