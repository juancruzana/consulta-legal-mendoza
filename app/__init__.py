# app/__init__.py - FACTORY PATTERN
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Instancias globales
db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    """Cargar usuario para Flask-Login"""
    from app.models.users import User
    return User.query.get(int(user_id))

def create_app(config_name='development'):
    """Factory para crear la aplicación Flask"""
    
    # Crear instancia de Flask
    app = Flask(__name__,
                template_folder=str(BASE_DIR / "app" / "templates"),
                static_folder=str(BASE_DIR / "app" / "static"))
    
    # Cargar configuración
    from app.config import config_by_name
    app.config.from_object(config_by_name[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    
    # Registrar Blueprints 
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.ai.routes import ai_bp
    
    app.register_blueprint(auth_bp)    # /auth/*
    app.register_blueprint(main_bp)    # /
    app.register_blueprint(ai_bp)      # /ai/*
    
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
    
    return app