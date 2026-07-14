import json
from urllib import response

from app.infraestructure.aws.repositories.bedrock_repository import (
    BedrockRepository,
)


class ToolRouter:

    def __init__(self):

        self.repository = BedrockRepository()

    def detect(
        self,
        message: str,
    ):

        prompt = f"""

Eres un enrutador de herramientas.

Debes responder únicamente un JSON válido.
No agregues explicaciones ni texto adicional.

Herramientas disponibles:

1. athena
Úsala cuando el usuario quiera:
- consultar tablas
- ejecutar SQL
- ver registros
- contar registros
- describir tablas
- consultar bases de datos

En este caso debes generar el SQL.

Ejemplos:

{{
    "tool": "athena",
    "query": "SHOW TABLES;"
}}

{{
    "tool": "athena",
    "query": "SELECT * FROM employees LIMIT 10;"
}}

{{
    "tool": "athena",
    "query": "SELECT COUNT(*) FROM employees;"
}}

2. s3

Úsala cuando el usuario quiera:
- listar archivos
- listar buckets
- ver datasets
- consultar archivos CSV o Parquet

Responde:

{{
    "tool": "s3"
}}

Si ninguna herramienta aplica responde:

{{
    "tool": null
}}

Pregunta:

{message}
"""

        response = self.repository.generate_response(
            prompt
        )
        
        print("========== TOOL ROUTER ==========")
        print(repr(response))
        
        clean_response = response.strip()

        if clean_response.startswith("```json"):
            clean_response = clean_response.replace(
                "```json",
                "",
                1,
            )

        if clean_response.startswith("```"):
            clean_response = clean_response.replace(
                "```",
                "",
                1,
            )

        if clean_response.endswith("```"):
            clean_response = clean_response[:-3]

        clean_response = clean_response.strip()

        print("========== JSON LIMPIO ==========")
        print(clean_response)

        try:

            return json.loads(clean_response)

        except Exception as e:

            print(e)

            return {
                "tool": None
            }