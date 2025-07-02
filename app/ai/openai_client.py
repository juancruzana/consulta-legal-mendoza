# Configuración OpenAI
import openai
from flask import current_app
from app.ai.prompts import SYSTEM_PROMPT

class LegalAiClient:
    def __init__(self):
        api_key = current_app.config.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY no está configurada en las variables de entorno")
        
        self.client = openai.OpenAI(api_key=api_key)
    
    def get_advice(self, promt):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": promt}
        ]
        

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content


