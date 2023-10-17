# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do seu aplicativo
RUN pip install -r requirements.txt

# Copie o código-fonte do seu aplicativo para o diretório de trabalho
COPY . .

# Exponha a porta em que o aplicativo FastAPI será executado
EXPOSE 8000

# Comando para iniciar o aplicativo com o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
