from flask import Blueprint, render_template, jsonify
from app.auth.forms import LoginForm

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)

@main_bp.route("/health", methods=["GET"])
def health():
    """Endpoint de healthcheck para Docker"""
    return jsonify({"status": "healthy", "message": "Application is running"}), 200

"""" 
@main_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    # Ejemplo de dashboard para usuarios logueados
    return render_template("dashboard.html", user=current_user)
"""
