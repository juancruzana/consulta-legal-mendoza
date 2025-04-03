from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar FastAPI
app = FastAPI()

# Inicializar cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/process-prompt")
async def process_prompt(request: PromptRequest):
    try:
        # Crear la llamada a OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente legal especializado en derecho argentino."},
                {"role": "user", "content": request.prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extraer la respuesta
        answer = response.choices[0].message.content
        
        return {
            "status": "success",
            "response": answer
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
