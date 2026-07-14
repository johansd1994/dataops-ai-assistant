from app.infraestructure.aws.clients.bedrock_client import BedrockClient


class BedrockRepository:

    def __init__(self):

        self.client = BedrockClient()

    def generate_response(self, prompt: str):

        return self.client.invoke(prompt)