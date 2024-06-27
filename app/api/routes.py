from fastapi import APIRouter
from pydantic import BaseModel

from app.services.openai_service import OpenAIService

router = APIRouter(prefix='/openai')


class OpenAIRequest(BaseModel):
    text: str


class OpenAIResponse(BaseModel):
    content: str


@router.post('/query', response_model=OpenAIResponse)
def consult_openai(request: OpenAIRequest):
    openai_service = OpenAIService()
    content = openai_service.get_text(request.text)
    return OpenAIResponse(content=content)
