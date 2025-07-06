# Usa uma imagem Node para buildar o frontend
FROM node:18 AS builder

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos package.json e package-lock.json / pnpm-lock.yaml
COPY package*.json ./

# Instala dependências
RUN npm install

# Copia o restante do projeto
COPY . .

# Builda o app para produção
RUN npm run build


# ----
# Agora cria o container final com nginx
FROM nginx:stable-alpine

# Remove a configuração default do nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos estáticos gerados pelo Vite
COPY --from=builder /app/dist /usr/share/nginx/html

# Copia uma config nginx customizada se quiser
# (opcional, por padrão nginx já serve em /)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta
EXPOSE 80

# Starta o nginx
CMD ["nginx", "-g", "daemon off;"]
