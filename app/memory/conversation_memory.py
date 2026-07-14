from typing import List


class ConversationMemory:

    def __init__(self):

        self.messages = []

    def add(
        self,
        role: str,
        content: str,
    ) -> None:

        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def history(self) -> List[dict]:

        return self.messages

    def clear(self) -> None:

        self.messages.clear()