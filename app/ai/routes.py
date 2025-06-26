from flask import Blueprint, request, jsonify
from app.ai.openai_client import LegalAiClient

ai_bp = Blueprint('ai', __name__)

@ai_bp.route("/consulta", methods=["POST"])
def consulta_legal():
    legal_ai_client = LegalAiClient()
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Falta el prompt"}), 400
    respuesta = legal_ai_client.get_advice(prompt)
    return jsonify({"respuesta": respuesta})
