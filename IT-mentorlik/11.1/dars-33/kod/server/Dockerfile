# 32-dars: MVP server (Express) uchun Dockerfile
# 33-dars: PostgreSQL versiyasi uchun ham aynan shu Dockerfile

# 1) Asos image: kichik va aniq versiya ("latest" emas!)
FROM node:20-alpine

# 2) Konteyner ichidagi ishchi papka
WORKDIR /app

# 3) Avval FAQAT package fayllar → npm install qatlami keshda qoladi
COPY package*.json ./
RUN npm install --omit=dev

# 4) Keyin kod (tez-tez o'zgaradi → faqat shu qatlam qayta yig'iladi)
COPY src ./src

# 5) Sozlamalar
ENV NODE_ENV=production \
    PORT=3000
EXPOSE 3000

# 6) Xavfsizlik: root emas, oddiy foydalanuvchi nomidan ishlash
RUN chown -R node:node /app
USER node

# 7) Healthcheck: /api/health javob bermasa — konteyner "unhealthy"
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:3000/api/health || exit 1

# 8) Ishga tushirish buyrug'i (exec shakli)
CMD ["node", "src/index.js"]
