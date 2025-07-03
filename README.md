# Email Classifier App

Este projeto é uma solução web para **classificar emails recebidos** em uma empresa do setor financeiro, usando **NLP + IA (GPT-3.5)** para:

- Classificar automaticamente o email como `Produtivo` ou `Improdutivo`.
- Gerar uma **resposta sugerida**, educada e contextual.


## Diferenciais implementados

- Pipeline modular com **services separados**:
  - NLP
  - AI
  - Cache (dict, facilmente trocável por Redis)
  - Extração de arquivos
- **Testes unitários e integrados**
- Makefile para CI/CD simples

## Tecnologias utilizadas

- **Python + Flask** (backend)
- **NLTK** (tokenização, stopwords, hash)
- **pdfminer.six** (extração de PDFs)
- **OpenAI GPT-3.5** (classificação e resposta)
- **Pytest** (testes)
- **pytest-cov** (cobertura)
- **Makefile** (automatizar tarefas)


## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/email-classifier-app.git
   cd email-classifier-app/backend
    ```

2. Instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Crie o .env e adicione sua API Key do OpenAI:
    ```bash
    OPENAI_API_KEY=sk-...
    ```

2. Rode o servidor:
    ```bash
    python app.py
    ```

## Como rodar os testes

```bash
make test-backend
```

Para ver a cobertura:
```bash
make coverage
```