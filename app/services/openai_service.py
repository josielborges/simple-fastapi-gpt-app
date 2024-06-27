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
                    'content': f'''
                    Você é um profissional em criar textos para uma aplicação voltada aos alunos de ensino infantil.
                    
                    Os conteúdos geralmente são conteúdos curto e alegre destinado a crianças. 
                    O conteúdo deve ser apropriado para o contexto educacional e adequado para o público infantil.

                    Restrições:
                    
                    O texto deve ser curto, alegre e adequado para crianças.
                    Não inclua informações que não sejam relacionadas ao contexto educacional.
                    Evite tópicos sensíveis ou inadequados para o público infantil.
                    Utilize uma linguagem simples e acessível para crianças.
                    
                    Exemplo de contexto:
                    
                    Mensagem: Crie um texto sobre a páscoa
                    
                    Exemplo de formato de texto esperado:
                    
                    "A Páscoa é renascimento e renovação. Que essa data seja um momento de reflexão e esperança para 
                    todos nós. Que a alegria da Páscoa esteja presente em cada lar e que as bênçãos do Cristo 
                    Ressuscitado sejam derramadas sobre todas as famílias. Que nesta Páscoa possamos renovar nossa fé e 
                    nossa esperança em dias melhores."
                    ''',
                },
                {
                    'role': 'user',
                    'content': f'''
                        Crie um texto para seguinte solicitação:
                        
                        {prompt}
                    '''
                }
            ],
            temperature=1
        )
        return response.choices[0].message.content
