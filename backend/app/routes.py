"""
Módulo routes

Define as rotas HTTP da aplicação Flask para processar uploads de arquivos ou textos.
Encaminha para o pipeline de processamento e retorna a classificação e resposta sugerida.
"""

from flask import Blueprint, request, jsonify
from app.pipeline import process_uploaded_file, process_raw_text

import logging
logging.basicConfig(level=logging.INFO)

routes = Blueprint('routes', __name__)

@routes.route("/upload", methods=["POST"])
def upload():
    """
    Rota POST /upload

    Recebe arquivos (TXT ou PDF) e/ou texto bruto via formulário multipart.
    Processa o conteúdo chamando o pipeline, que realiza extração, pré-processamento,
    classificação via IA e armazenamento em cache.

    O endpoint aceita:
    - múltiplos arquivos enviados no campo "file"
    - texto enviado no campo "text"

    Retorna:
        JSON:
        {
            "results": [
                {
                    "type": "file" ou "text",
                    "file": "nome_do_arquivo.txt" (quando for arquivo),
                    "categoria": "Produtivo" ou "Improdutivo",
                    "resposta_sugerida": "..."
                },
                ...
            ]
        }

    Status Codes:
        - 200: Sucesso no processamento (mesmo com alguns erros parciais nos arquivos).
        - 400: Nenhum arquivo ou texto foi enviado.
    """
    results = []

    files = request.files.getlist("file")
    for file in files:
        if file.filename == '':
            continue
        try:
            classification = process_uploaded_file(file)
            logging.info(f"--- {file.filename} Classificação --- {classification}")
            results.append({
                "type": "file",
                "file": file.filename,
                "categoria": classification.get("categoria"),
                "resposta_sugerida": classification.get("resposta_sugerida")
            })
        except ValueError as e:
            logging.error(f"Erro ao processar {file.filename}: {str(e)}", exc_info=True)
            results.append({
                "type": "file",
                "file": file.filename,
                "error": str(e)
            })

    raw_text = request.form.get("text", "").strip()
    if raw_text:
        try:
            classification = process_raw_text(raw_text)
            logging.info(f"--- Texto inserido Classificação --- {classification}")
            results.append({
                "type": "text",
                "categoria": classification.get("categoria"),
                "resposta_sugerida": classification.get("resposta_sugerida")
            })
        except ValueError as e:
            logging.error("Erro ao processar texto inserido.", exc_info=True)
            results.append({
                "type": "text",
                "error": str(e)
            })

    if not results:
        return jsonify({"error": "Nenhum arquivo ou texto enviado."}), 400

    return jsonify({"results": results})
