from flask import Flask, render_template, request
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

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = ""
    if request.method == "POST":
        consulta = request.form.get("consulta")
        if consulta:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": consulta}]
            )
            respuesta = completion.choices[0].message.content
    return render_template("index.html", respuesta=respuesta)
