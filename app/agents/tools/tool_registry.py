from typing import Dict

from app.agents.tools.base_tool import BaseTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    def detect(self, message: str):

        text = message.lower()

        if any(word in text for word in [
            "athena",
            "tabla",
            "tablas",
            "describe",
            "select",
            "registro",
            "registros",
        ]):

            return {
                "tool": "athena",
                "query": message,
            }

        if any(word in text for word in [

            "bucket",

            "buckets",

            "archivo",

            "archivos",

            "csv",

            "dataset",

            "datasets",

            "s3",

            "objeto",

            "objetos",

        ]):

            return {
                "tool": "s3",
                "query": message,
            }

        return None