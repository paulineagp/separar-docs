FROM python:3.11-slim  # Mais específico e menor imagem

WORKDIR /app  # Diretório mais comum

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
