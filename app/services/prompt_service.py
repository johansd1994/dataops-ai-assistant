from app.prompts.system_prompt import SYSTEM_PROMPT


class PromptService:
    """
    Builds prompts for the AI Agent.
    """

    @staticmethod
    def build_prompt(
        message: str,
        history: list,
    ) -> str:

        conversation = ""

        for item in history:

            role = item["role"].capitalize()

            conversation += f"{role}: {item['content']}\n"

        prompt = f"""
{SYSTEM_PROMPT}

====================================

Conversation History

{conversation}

====================================

Current User Question

{message}

====================================

Answer:
"""

        return prompt

    @staticmethod
    def build_tool_prompt(
        question: str,
        tool_result,
        history: list,
    ) -> str:

        conversation = ""

        for item in history:

            role = item["role"].capitalize()

            conversation += f"{role}: {item['content']}\n"

        return f"""
{SYSTEM_PROMPT}

====================================

Conversation History

{conversation}

====================================

Tool Result

{tool_result}

====================================

Current User Question

{question}

====================================

Use ONLY the tool result to answer the question.
Do not invent information.
"""