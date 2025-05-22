import os
from dotenv import load_dotenv

# Normalizar la ruta absoluta al .env.local
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env.local'))
print(f"Ruta normalizada: {dotenv_path}")

loaded = load_dotenv(dotenv_path=dotenv_path)
print(f"¿Se cargó el archivo?: {loaded}")

api_key = os.getenv("OPENAI_API_KEY")
print(f"Clave cargada: {api_key}")
