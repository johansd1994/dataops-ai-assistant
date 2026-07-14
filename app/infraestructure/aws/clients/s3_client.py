from app.infraestructure.aws.clients.base_client import BaseAWSClient

class S3Client(BaseAWSClient):

    def __init__(self):

        super().__init__()

        self.client = self.session.client(

            "s3",

            config=self.config

        )   
    
    def list_objects(
        self,
        bucket: str,
    ):

        return self.client.list_objects_v2(
            Bucket=bucket,
        )


    def list_buckets(self):

        return self.client.list_buckets()