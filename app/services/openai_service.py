import os

from dotenv import load_dotenv
from openai import OpenAI

from app.utils.helpers import OpenaiModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class OpenAIService:

    def __init__(self, model=OpenaiModel.GPT_3_5.value):
        self.model = model
        pass

    def get_text(self, prompt) -> str:
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': prompt,
                }
            ],
            temperature=1
        )
        return response.choices[0].message.content
