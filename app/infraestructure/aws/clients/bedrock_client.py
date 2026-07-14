import json
from urllib import response

from app.infraestructure.aws.clients.base_client import BaseAWSClient


class BedrockClient(BaseAWSClient):

    def __init__(self):

        super().__init__()

        self.client = self.session.client(
            "bedrock-runtime",
            config=self.config
        )

        self.logger.info("Bedrock Client initialized.")

    def invoke(self, prompt: str) -> str:

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = self.client.invoke_model(
            modelId=self.settings.BEDROCK_INFERENCE_PROFILE_ID,
            body=json.dumps(body)
        )

        response_body = json.loads(
            response["body"].read()
        )

        return response_body["content"][0]["text"]