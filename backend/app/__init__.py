"""
Módulo de inicialização da aplicação Flask.

Este módulo carrega variáveis de ambiente a partir do arquivo .env,
configura o Swagger para documentação da API e registra as rotas do blueprint.

Ele também garante que a pasta de uploads exista para armazenar arquivos temporários.
"""

from flask import Flask
from dotenv import load_dotenv
import os
from flasgger import Swagger
from app.routes import routes
from flask_cors import CORS


# Carregar variáveis do .env
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=dotenv_path)

# Inicializar Flask e Swagger
app = Flask(__name__)
CORS(app)
swagger = Swagger(app, template_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs', 'openapi.yaml')))
app.register_blueprint(routes)

# Garantir que o diretório de uploads exista
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

