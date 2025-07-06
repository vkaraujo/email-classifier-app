# Usar imagem oficial Python slim para menos peso
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do projeto
COPY . /app

# Instalar dependências do sistema (p.ex. para pdfminer e outros pacotes C)
RUN apt-get update && \
    apt-get install -y build-essential poppler-utils && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt stopwords

# Definir variável de ambiente
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Expor porta padrão do Flask
EXPOSE 5000

# Comando padrão para iniciar
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
