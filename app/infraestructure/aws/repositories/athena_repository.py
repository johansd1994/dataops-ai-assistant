import time

from app.core.settings import settings
from app.infraestructure.aws.clients.athena_client import AthenaClient


class AthenaRepository:

    def __init__(self):

        self.client = AthenaClient()

    def execute_query(
        self,
        query: str,
    ):

        response = self.client.start_query(

            query=query,

            database=settings.ATHENA_DATABASE,

            output_location=settings.ATHENA_OUTPUT_LOCATION,

            workgroup=settings.ATHENA_WORKGROUP,
        )

        execution_id = response["QueryExecutionId"]

        while True:

            execution = self.client.get_query_status(
                execution_id
            )

            state = execution[
                "QueryExecution"
            ][
                "Status"
            ][
                "State"
            ]

            if state == "SUCCEEDED":
                break

            if state in [
                "FAILED",
                "CANCELLED",
            ]:

                raise Exception(
                    f"Athena query {state}"
                )

            time.sleep(1)

        results = self.client.get_results(
            execution_id
        )

        return self._parse_results(results)

    def _parse_results(self, results):

        rows = results["ResultSet"]["Rows"]

        data = []

        for row in rows:

            values = []

            for column in row["Data"]:

                values.append(
                    column.get("VarCharValue")
                )

            data.append(values)

        return data