from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # Busca automáticamente .env en la misma carpeta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tirá un número del 1 al 10"}
    ]
)

print(response.choices[0].message.content)
