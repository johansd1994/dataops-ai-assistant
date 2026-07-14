from app.infraestructure.aws.clients.base_client import BaseAWSClient


class AthenaClient(BaseAWSClient):

    def __init__(self):

        super().__init__()

        self.client = self.session.client(
            "athena",
            config=self.config,
        )

        self.logger.info(
            "Athena Client initialized."
        )

    def start_query(
        self,
        query: str,
        database: str,
        output_location: str,
        workgroup: str,
    ):

        return self.client.start_query_execution(

            QueryString=query,

            QueryExecutionContext={
                "Database": database,
            },

            ResultConfiguration={
                "OutputLocation": output_location,
            },

            WorkGroup=workgroup,
        )

    def get_query_status(
        self,
        execution_id: str,
    ):

        return self.client.get_query_execution(
            QueryExecutionId=execution_id,
        )

    def get_results(
        self,
        execution_id: str,
    ):

        return self.client.get_query_results(
            QueryExecutionId=execution_id,
        )