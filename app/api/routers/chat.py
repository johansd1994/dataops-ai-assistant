from fastapi import APIRouter

from app.api.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat"
)

chat_service = ChatService()


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    response = chat_service.chat(request.message)

    return ChatResponse(
        response=response
    )