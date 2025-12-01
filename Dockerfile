# Usa Python leve
FROM python:3.11-slim

# Define pasta de trabalho
WORKDIR /app

# (Solução Blindada) Instala as bibliotecas DIRETAMENTE para garantir que o Python ache elas
RUN pip install click pillow rich

# Copia o código do projeto para dentro
COPY . .

# Comando final
ENTRYPOINT ["python", "main.py"]