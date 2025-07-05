def classification_prompt(cleaned_text):
    """
    Gera um prompt estruturado para ser enviado a um modelo de linguagem (LLM),
    instruindo-o a classificar o email como "Produtivo" ou "Improdutivo"
    e sugerir uma resposta curta e educada em formato JSON.

    Definições usadas na classificação:
    - "Produtivo": Emails que requerem ação ou resposta (suporte, dúvidas, etc).
    - "Improdutivo": Emails que não necessitam de ação imediata (agradecimentos, felicitações).

    Args:
        cleaned_text (str): O texto do email já pré-processado (sem stopwords, etc).

    Returns:
        str: Um prompt formatado que orienta o modelo a responder em JSON,
             contendo a categoria e a resposta sugerida.
    """
    return f"""
Você é um assistente especializado em analisar emails recebidos por uma empresa do setor financeiro.

Seu trabalho é:
1. Classificar o email como "Produtivo" ou "Improdutivo", de acordo com as definições abaixo.
2. Sugerir uma resposta curta e educada, caso necessário.

**Definições:**
- "Produtivo": Emails que requerem uma ação ou resposta específica. Exemplos incluem:
    • solicitações de suporte técnico
    • atualização sobre casos em aberto
    • dúvidas sobre o sistema
    • questionamentos financeiros ou operacionais
- "Improdutivo": Emails que não necessitam de uma ação imediata. Exemplos incluem:
    • mensagens de felicitações
    • simples agradecimentos
    • emails genéricos sem pedidos claros

Analise o seguinte email:

\"\"\"{cleaned_text}\"\"\"

Responda apenas no seguinte formato JSON, sem comentários adicionais:

{{
  "categoria": "<Produtivo ou Improdutivo>",
  "resposta_sugerida": "<sua resposta aqui>"
}}
"""
