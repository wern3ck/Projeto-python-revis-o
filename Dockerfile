# Imagem base do Python
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os ficheiros da aplicação
COPY . /app

# Instalar o pytest
RUN pip install --no-cache-dir pytest

# Comando para iniciar o programa
CMD ["python", "calculadora.py"]