# config.py - CONFIGURACIONES GLOBALES
import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent

class Config:
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-in-production")
    
    # Configuración de OpenAI
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    
    # Configuración de la base de datos
    MYSQL_USER = os.environ.get("DB_USER", "appuser")
    MYSQL_PASSWORD = os.environ.get("DB_PASSWORD", "1234")
    MYSQL_HOST = os.environ.get("DB_HOST", "db")
    MYSQL_PORT = os.environ.get("DB_PORT","3306")
    MYSQL_DB = os.environ.get("DB_NAME", "legal_assistent")
    
    # URI de conexión para SQLAlchemy (MySQL con PyMySQL)
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Login
    LOGIN_VIEW = 'auth.login'
    LOGIN_MESSAGE = 'Debes iniciar sesión para acceder.'

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Muestra las queries SQL en consola

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    SQLALCHEMY_ECHO = False

# Diccionario para seleccionar configuración
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}