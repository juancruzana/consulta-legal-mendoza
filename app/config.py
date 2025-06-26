# config.py - CONFIGURACIONES GLOBALES
import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent

class Config:
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-in-production")
    
    # Configuración de la base de datos
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "skatebor10")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.environ.get("DB_PORT","3306")
    MYSQL_DB = os.environ.get("MYSQL_DB", "legal_assistent")
    
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