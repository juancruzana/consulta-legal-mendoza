FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar TODO el proyecto
COPY . .

# dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]