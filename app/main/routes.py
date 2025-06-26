from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.auth.forms import LoginForm

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)

"""" 
@main_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    # Ejemplo de dashboard para usuarios logueados
    return render_template("dashboard.html", user=current_user)
"""
