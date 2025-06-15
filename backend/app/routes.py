from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os
from pathlib import Path

# Configuración mejorada
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH if ENV_PATH.exists() else None)

app = Flask(__name__,
    template_folder=str(BASE_DIR / "frontend" / "templates"),
    static_folder=str(BASE_DIR / "frontend" / "static")
)

# Configuración OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Eres un abogado experto en derecho argentino. Responde consultas legales sobre:
- Código Civil y Comercial
- Leyes laborales
- Derecho penal
- Derecho administrativo
Proporciona información precisa y actualizada, citando normas cuando sea relevante.
Indica cuando una consulta requiera asesoramiento profesional presencial.
"""

@app.route("/", methods=["GET"])
def index():
    # Renderiza el template principal (index.html)
    return render_template("index.html")

@app.route("/consulta", methods=["POST"])
def consulta_legal():
    try:
        data = request.get_json()
        consulta = data.get("consulta", "").strip()
        
        if not consulta:
            return jsonify({"error": "Consulta vacía"}), 400
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": consulta}
            ],
            temperature=0.3,
            max_tokens=300
        )
        
        return jsonify({
            "respuesta": response.choices[0].message.content
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500