from urllib import response
from app.agents.tool_router import ToolRouter
from app.agents.base_agent import BaseAgent

from app.memory.conversation_memory import ConversationMemory

from app.infraestructure.aws.repositories.bedrock_repository import (
    BedrockRepository,
)

from app.agents.tools.tool_registry import ToolRegistry
from app.agents.tools.athena_tool import AthenaTool
from app.agents.tools.s3_tool import S3Tool

from app.services.prompt_service import PromptService


class DataOpsAgent(BaseAgent):

    def __init__(self):

        self.memory = ConversationMemory()

        self.repository = BedrockRepository()

        self.registry = ToolRegistry()

        self.router = ToolRouter()

        self.registry.register(AthenaTool())

        self.registry.register(S3Tool())


    def chat(self, message: str) -> str:

        self.memory.add(
            "user",
            message
        )

        history = self.memory.history()

        tool_call = self.router.detect(message)

        print(tool_call)

        if tool_call.get("tool"):

            tool = self.registry.get(
                tool_call["tool"]
            )

            query = tool_call.get("query")

            tool_result = tool.execute(query)

            print("========== TOOL RESULT ==========")
            print(tool_result)

            prompt = PromptService.build_tool_prompt(
                question=message,
                tool_result=tool_result,
                history=history,
            )

            response = self.repository.generate_response(
                prompt
            )

        else:

            prompt = PromptService.build_prompt(
                message=message,
                history=history,
            )

            response = self.repository.generate_response(
                prompt
            )

        self.memory.add(
            "assistant",
             response,
        )

        return response