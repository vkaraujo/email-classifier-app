from flask import Blueprint, request, jsonify
from app.pipeline import process_uploaded_file

import logging
logging.basicConfig(level=logging.INFO)

routes = Blueprint('routes', __name__)

@routes.route("/")
def hello():
    return "Hello from Flask!"

@routes.route("/upload", methods=["POST"])
def upload_file():
    file_or_error = get_uploaded_file(request)
    if isinstance(file_or_error, dict):
        return jsonify(file_or_error), 400

    file = file_or_error

    try:
        classification = process_uploaded_file(file)
        logging.info(f"--- Classificação --- {classification}")
        return jsonify({
            "message": "Arquivo processado com sucesso.",
            "categoria": classification.get("categoria"),
            "resposta_sugerida": classification.get("resposta_sugerida")
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def get_uploaded_file(req):
    if 'file' not in req.files:
        return {"error": "No file part"}
    file = req.files['file']
    if file.filename == '':
        return {"error": "No selected file"}
    return file
