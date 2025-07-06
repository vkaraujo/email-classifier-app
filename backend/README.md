## 🔥 Rodando o backend com Docker

```bash
cd backend
docker build -t email-classifier-backend .
docker run -p 5000:5000 --env OPENAI_API_KEY=suachaveaqui email-classifier-backend
```

Acesse a API e Swagger UI em: http://localhost:5000/apidocs