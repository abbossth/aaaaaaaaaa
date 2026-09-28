# 32-dars slaydlari: Dockerfile 📝

## 1-slayd
📝 **Dockerfile** = image tayyorlash **retsepti** 🍰

## 2-slayd — Anatomiya
```dockerfile
FROM node:20-alpine          # qaysi asosdan
WORKDIR /app                 # ichki papka (cd + mkdir)
COPY package*.json ./        # fayllarni nusxalash
RUN npm install --omit=dev   # yig'ish vaqtida buyruq
COPY src ./src
ENV PORT=3000                # muhit o'zgaruvchisi
EXPOSE 3000                  # hujjat: qaysi port
USER node                    # root emas!
CMD ["node", "src/index.js"] # konteyner ishga tushganda
```

## 3-slayd — RUN vs CMD
| `RUN` | `CMD` |
|---|---|
| **Build** paytida (image yasalayotganda) | **Run** paytida (konteyner boshlanganda) |
| Ko'p bo'lishi mumkin | Faqat oxirgisi ishlaydi |

## 4-slayd — Kesh: tartib muhim! 🥞
❌ Yomon:
```dockerfile
COPY . .
RUN npm install        # har bir kod o'zgarishida qayta 2 daqiqa 😴
```
✅ Yaxshi:
```dockerfile
COPY package*.json ./
RUN npm install        # package.json o'zgarmasa — CACHED ⚡
COPY src ./src
```
Qoida: **kam o'zgaradigan — yuqorida, ko'p o'zgaradigan — pastda**

## 5-slayd — .dockerignore
`node_modules` · `.env` 🔐 · `.git` · `db.json` — image'ga kirmasin!

## 6-slayd — Tag = versiya
`login/mvp-server:0.1.0` → `login/mvp-server:latest`
SemVer: **MAJOR.MINOR.PATCH** — 1.4.2
⚠️ Production'da `latest` ga ishonmang — aniq versiya yozing

## 7-slayd — Multi-stage build
```dockerfile
FROM node:20-alpine AS build     # 1: yig'ish (~400 MB)
RUN npm run build
FROM nginx:alpine                # 2: faqat natija (~50 MB)
COPY --from=build /app/dist /usr/share/nginx/html
```

## 8-slayd — Xavfsizlik checklist ✅
- Aniq versiyali, kichik asos (`-alpine`, `-slim`)
- `USER node` (root emas)
- Maxfiy ma'lumot image'da **yo'q** (`.env` → `-e` yoki secrets)
- `HEALTHCHECK`
