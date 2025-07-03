def classification_prompt(cleaned_text):
    return f"""
Você é um assistente que classifica emails recebidos para uma empresa do setor financeiro.

Analise o seguinte texto e faça duas coisas:
1. Classifique-o como "Produtivo" ou "Improdutivo"
2. Sugira uma resposta curta e educada para o email, caso necessário.

Email: \"\"\"{cleaned_text}\"\"\"

Responda no seguinte formato JSON:

{{
  "categoria": "<Produtivo ou Improdutivo>",
  "resposta_sugerida": "<sua resposta aqui>"
}}
"""
