"""
Módulo responsável por interagir com a API da OpenAI para classificar emails
e sugerir respostas automáticas.

Ele constrói um prompt com o texto já pré-processado, envia ao modelo GPT-3.5-turbo
e espera como retorno um JSON com a classificação ("Produtivo" ou "Improdutivo")
e uma resposta sugerida.

Caso o JSON não possa ser decodificado ou ocorra algum erro, o módulo trata o caso
retornando informações padronizadas.
"""

import os
import json
import logging
from openai import OpenAI
from app.prompts import classification_prompt

logging.basicConfig(level=logging.INFO)

def classify_and_suggest(cleaned_text):
    """
    Envia o texto limpo para o GPT-3.5 com um prompt de classificação,
    solicitando a categoria do email e uma resposta curta.

    Args:
        cleaned_text (str): O texto do email já pré-processado.

    Returns:
        dict: Um dicionário no formato:
            {
                "categoria": "<Produtivo | Improdutivo | Desconhecido | Erro>",
                "resposta_sugerida": "<resposta curta>"
            }
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = classification_prompt(cleaned_text)

    logging.info("Enviando prompt ao GPT-3.5...")
    logging.debug(f"Prompt enviado: {prompt}")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        logging.error("Resposta do GPT não pôde ser decodificada como JSON.", exc_info=True)
        return {
            "categoria": "Desconhecido",
            "resposta_sugerida": response.choices[0].message.content.strip()
        }
    except Exception as e:
        logging.error("Erro ao consultar o GPT-3.5.", exc_info=True)
        return {
            "categoria": "Erro",
            "resposta_sugerida": f"Não foi possível gerar uma resposta automática: {str(e)}"
        }
