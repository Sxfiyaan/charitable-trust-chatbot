from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"]
)


@router.get("/")
def chat_status():
    return {
        "status": "Chat Router Working"
    }


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    ai_response = ChatService.get_response(
        request.session_id,
        request.message
    )

    return ChatResponse(
        response=ai_response
    )