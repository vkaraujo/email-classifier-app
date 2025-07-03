from flask import Blueprint, request, jsonify
from app.services import process_uploaded_file

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
        filename, text_content = process_uploaded_file(file)
        print(f"--- Conteúdo extraído de {filename} ---")
        print(text_content[:1000])
        return jsonify({"message": f"Arquivo {filename} processado com sucesso."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def get_uploaded_file(req):
    if 'file' not in req.files:
        return {"error": "No file part"}
    file = req.files['file']
    if file.filename == '':
        return {"error": "No selected file"}
    return file
