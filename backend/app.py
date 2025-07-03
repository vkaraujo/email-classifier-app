from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask!"

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    text = data.get("text", "")
    # Aqui vamos depois processar o texto e chamar GPT
    return jsonify({"categoria": "Exemplo", "resposta_sugerida": f"Recebi: {text}"})


if __name__ == "__main__":
    app.run(debug=True)
