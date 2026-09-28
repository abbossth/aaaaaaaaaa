# 32-dars amaliy topshiriq (jamoaviy)

Asos: jamoangiz reposidagi `server/` (25-darsdagi `mvp-skelet`). Namuna: `kod/server/Dockerfile`, `kod/server/.dockerignore`.

## 🟢 Oson (+5 XP)
1. `server/Dockerfile` va `.dockerignore` yarating. `docker build -t mvp-server .` → `docker run -p 3000:3000` → `curl localhost:3000/api/health`.
2. `docker images` dan image hajmini yozing.

## 🟡 O'rta (+10 XP)
3. `src/app.js` ni o'zgartirib qayta yig'ing. Qaysi qatlamlar `CACHED` bo'ldi? Keyin `COPY . .` ni `npm install` dan **oldin** qo'yib, farqni o'lchang (`time docker build ...`).
4. Image'ni `0.1.0` tag bilan Docker Hub'ga push qiling. Boshqa jamoa sizning image'ingizni ishga tushirsin.
5. `docker run -e PORT=4000 -p 4000:4000 ...` — port env orqali o'zgarishini tekshiring.

## 🔴 Qiyin (+20 XP)
6. `web/` uchun multi-stage Dockerfile (`kod/web/Dockerfile`, `kod/web/nginx.conf`). Image hajmini `node:20-alpine` bilan solishtiring.
7. `docker scout quickview` (yoki `trivy image`) bilan image'dagi zaifliklarni (CVE) tekshiring. Natijani jamoa kanaliga.
8. Jamoa README'siga "Docker bilan ishga tushirish" bo'limini qo'shing.
