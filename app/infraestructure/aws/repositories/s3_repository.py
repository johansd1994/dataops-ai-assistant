from app.core.settings import settings

from app.infraestructure.aws.clients.s3_client import (
    S3Client,
)


class S3Repository:

    def __init__(self):

        self.client = S3Client()

    def list_files(self):

        response = self.client.list_objects(
            settings.S3_BUCKET_NAME
        )

        files = []

        for obj in response.get(
            "Contents",
            [],
        ):

            files.append(
                obj["Key"]
            )

        return files

    def list_buckets(self):

        response = self.client.list_buckets()

        buckets = []

        for bucket in response["Buckets"]:

            buckets.append(
                bucket["Name"]
            )

        return buckets