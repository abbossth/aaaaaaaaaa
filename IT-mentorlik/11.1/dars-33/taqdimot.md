# 33-dars slaydlari: Compose 🎼

## 1-slayd
💀 Konteyner o'ldi → `db.json` ham o'ldi. **Ma'lumot konteynerdan tashqarida yashashi kerak!**

## 2-slayd — Network 🌐
```
┌──────── mvp-net (bridge) ────────┐
│  [server] ──"db:5432"──▶ [db]    │   ← nom = DNS
└──────────────────────────────────┘
     ▲ -p 3000:3000
  brauzer
```
⚠️ Konteyner ichida `localhost` = **konteynerning o'zi**, kompyuter emas!

## 3-slayd — Volume 💾
| | Named volume | Bind mount |
|---|---|---|
| Sintaksis | `-v pgdata:/var/lib/postgresql/data` | `-v ./sayt:/usr/share/nginx/html` |
| Qayerda? | Docker boshqaradi | Kompyuteringizdagi papka |
| Qachon? | **Baza** ma'lumotlari | Ishlab chiqishda kod, konfiglar |

## 4-slayd — Muammo: 5 ta uzun buyruq 😩
`network create` + `volume create` + `run db ...` + `build` + `run server ...`

## 5-slayd — Yechim: docker-compose.yml 🎼
```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U mvp"]
  server:
    build: ./server
    environment:
      DATABASE_URL: postgres://mvp:${DB_PASSWORD}@db:5432/mvp
    ports: ["3000:3000"]
    depends_on:
      db: { condition: service_healthy }
volumes:
  pgdata:
```
Tarmoq **avtomatik** yaratiladi!

## 6-slayd — Buyruqlar
```bash
docker compose up -d --build   # yig'ish + ishga tushirish
docker compose ps / logs -f server / exec db psql -U mvp
docker compose down            # volume qoladi
docker compose down -v         # ⚠️ volume ham o'chadi
```

## 7-slayd — depends_on tuzog'i
`depends_on: [db]` — faqat **ishga tushish tartibi**, baza **tayyor**ligini kutmaydi!
✅ `condition: service_healthy` + `healthcheck`

## 8-slayd — Maxfiylik
`.env` (git'ga ❌) → `${DB_PASSWORD}` · `.env.example` (git'ga ✅)
