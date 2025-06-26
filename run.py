# run.py - ARCHIVO PRINCIPAL PARA EJECUTAR
from app import create_app
import os

# Determinar el ambiente (desarrollo/producción)
config_name = os.environ.get('FLASK_ENV', 'development')

# Crear la aplicación Flask
app = create_app(config_name)

if __name__ == '__main__':
    # Solo para desarrollo - En producción usa Gunicorn/uWSGI
    app.run(debug=True, host='0.0.0.0', port=5000)