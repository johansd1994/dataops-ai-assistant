import json

import boto3

MODEL_ID = "global.anthropic.claude-sonnet-4-6"

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 200,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hola, responde únicamente: Conexión exitosa."
                }
            ]
        }
    ]
}

response = client.invoke_model(
    modelId=MODEL_ID,
    body=json.dumps(body)
)

response_body = json.loads(
    response["body"].read()
)

print(json.dumps(response_body, indent=2, ensure_ascii=False))