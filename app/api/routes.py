from fastapi import APIRouter
from pydantic import BaseModel

from app.services.openai_service import OpenAIService

router = APIRouter(prefix='/openai')


class OpenAIRequest(BaseModel):
    prompt: str


class OpenAIResponse(BaseModel):
    content: str


@router.post('/requisicao', response_model=OpenAIResponse)
def consult_openai(request: OpenAIRequest):
    openai_service = OpenAIService()
    content = openai_service.get_text(request.prompt)
    return OpenAIResponse(content=content)
