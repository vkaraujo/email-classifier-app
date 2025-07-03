from flask import Flask
from dotenv import load_dotenv
import os
from app.routes import routes

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
app.register_blueprint(routes)

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
