from app.infraestructure.aws.repositories.athena_repository import (
    AthenaRepository,
)


class AthenaTool:

    name = "athena"

    def __init__(self):

        self.repository = AthenaRepository()

    def execute(
        self,
        query: str,
    ):

        return self.repository.execute_query(query)

    def _translate(
        self,
        query: str,
    ) -> str:

        text = query.lower()

        if "tabla" in text and "describe" not in text:

            return "SHOW TABLES;"

        if "describe" in text:

            table = text.replace(
                "describe",
                ""
            ).strip()

            return f"DESCRIBE {table};"

        if "primeros" in text:

            table = text.split()[-1]

            return (
                f"SELECT * "
                f"FROM {table} "
                f"LIMIT 10;"
            )

        return query