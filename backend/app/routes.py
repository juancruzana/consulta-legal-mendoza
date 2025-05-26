from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from openai import OpenAI
import os
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

app = Flask(
    __name__,
    template_folder="../../frontend/templates",
    static_folder="../../frontend/static"
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

rol_system = """Eres un abogado experto en derecho argentino. Responde consultas legales sobre: 
- codigo civil y comercial.
- leyes laborales 
-derecho penal
-derecho administrativo
Proporcionando informacion precisa y actualizada, citando normas cuando sea relevante.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/consulta", methods=["POST"])
def consulta():
    data = request.get_json()
    pregunta = data.get("consulta", "")

    if not pregunta:
        return jsonify({"error": "Consulta vacía"}), 400

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": rol_system},{"role": "user", "content": pregunta}],
    temperature=1.2,
    top_p=1.0,
    presence_penalty=0.6,
    frequency_penalty=0.3
)

    respuesta = completion.choices[0].message.content
    return jsonify({"respuesta": respuesta})

