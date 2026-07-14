from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for every AI Agent.
    """

    @abstractmethod
    def chat(self, message: str) -> str:
        """
        Execute an agent conversation.
        """
        pass