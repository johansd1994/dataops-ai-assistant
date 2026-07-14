from app.infraestructure.aws.repositories.athena_repository import (
    AthenaRepository,
)

repository = AthenaRepository()

response = repository.execute_query(
    "SHOW TABLES;"
)

print(response)