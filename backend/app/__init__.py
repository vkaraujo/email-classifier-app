from flask import Flask
from dotenv import load_dotenv
import os
from app.routes import routes

load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes)

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
