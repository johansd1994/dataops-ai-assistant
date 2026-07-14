from app.agents.dataops_agent import DataOpsAgent


class ChatService:

    def __init__(self):

        self.agent = DataOpsAgent()

    def chat(self, message: str):

        return self.agent.chat(message)