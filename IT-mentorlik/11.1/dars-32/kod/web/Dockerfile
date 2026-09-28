# 32-dars (qiyin topshiriq): React (Vite) frontend — multi-stage build
# Joylash: mvp-skelet/web/Dockerfile

# 1-bosqich: yig'ish (build) — node bilan
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build            # natija: /app/dist

# 2-bosqich: faqat tayyor statik fayllar — nginx bilan (node_modules yo'q!)
FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
