# 32-dars tezkor test

1. `RUN` va `CMD` farqi? — `RUN` image yig'ilayotganda, `CMD` konteyner ishga tushganda bajariladi
2. Nega `package.json` kodning qolgan qismidan oldin nusxalanadi? — `npm install` qatlami keshda qolishi uchun
3. `.dockerignore` ga nega `.env` yoziladi? — Maxfiy ma'lumot image'ga tushib qolmasligi uchun
4. `docker build -t app .` dagi nuqta? — Build context (joriy papka)
5. `node:20-alpine` ning afzalligi? — Kichik hajm (Alpine Linux asosida)
6. Multi-stage build nima uchun? — Yig'ish vositalarisiz, faqat natijadan iborat kichik image olish
7. Nega `USER node`? — Konteyner root huquqida ishlamasligi uchun (xavfsizlik)
