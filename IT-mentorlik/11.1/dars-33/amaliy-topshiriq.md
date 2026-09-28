# 33-dars amaliy topshiriq (jamoaviy)

Namuna: `kod/docker-compose.yml`, `kod/server/` (PostgreSQL bilan ishlaydigan MVP server, `pg` kutubxonasi).

## 🟢 Oson (+5 XP)
1. `kod/` papkasini ishga tushiring: `cp .env.example .env && docker compose up -d --build`. `curl` bilan item qo'shing, `docker compose down` → `up` → item joyidami?
2. Adminer'ga kiring (`localhost:8081`, server: `db`, user: `mvp`) va `items` jadvalini ko'ring.

## 🟡 O'rta (+10 XP)
3. Jamoangiz MVP'sini `db.json` dan PostgreSQL'ga o'tkazing (`kod/server/src/app.js` namunasi bo'yicha) va repo ildiziga `docker-compose.yml` qo'shing.
4. `web` xizmatini qo'shing (32-darsdagi multi-stage Dockerfile, `ports: ["8080:80"]`). Brauzerda `localhost:8080` → frontend → `/api` → server → db. To'liq zanjir!

## 🔴 Qiyin (+20 XP)
5. `docker-compose.override.yml` — ishlab chiqish rejimi: `server/src` bind mount + `node --watch`. Kodni o'zgartirsangiz konteyner avtomatik qayta yuklansin.
6. Backup: `docker compose exec db pg_dump -U mvp mvp > backup.sql` va tiklash skripti `restore.sh`.
7. `db` xizmatida `ports` yo'qligi nega xavfsizroq? README'ga 3 jumla yozing.
