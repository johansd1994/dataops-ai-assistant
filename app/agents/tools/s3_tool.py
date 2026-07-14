from email.mime import text

from app.agents.tools.base_tool import BaseTool

from app.infraestructure.aws.repositories.s3_repository import (
    S3Repository,
)


class S3Tool(BaseTool):

    name = "s3"

    description = "Read objects from Amazon S3."

    def __init__(self):

        self.repository = S3Repository()

    def execute(
        self,
        query=None,
    ):

        if query is None:
            return self.repository.list_files()

        text = query.lower()

        if "bucket" in text:
            return self.repository.list_buckets()

        return self.repository.list_files()