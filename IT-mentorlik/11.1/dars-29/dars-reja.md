# 29-dars. Nginx: server block, reverse proxy, loglar

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "Nginx o'rnatilib, server block va reverse-proxy (proxy_pass http://127.0.0.1:3000) sozlanadi"

## Maqsad
- Web server va reverse proxy nima ekanini tushunadi: nega Node ilova to'g'ridan-to'g'ri 80-portda emas, Nginx ortida turadi.
- Nginx'ni o'rnatadi va konfiguratsiya tuzilishini biladi: `/etc/nginx/sites-available`, `sites-enabled`, `server {}`, `location {}`.
- React build'ni (statik fayllar) Nginx orqali tarqatadi, `/api` so'rovlarini Express'ga yo'naltiradi (`proxy_pass`).
- `nginx -t`, `systemctl reload nginx`, `curl -I` va loglar (`access.log`, `error.log`) bilan diagnostika qiladi.
- 502/404 xatolarini topib tuzatadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Nginx dunyodagi eng ko'p ishlatiladigan web serverlardan biri. *"Siz ochgan saytlarning katta qismi ortida — Nginx. Uning ishi: mehmonlarni kutib olish va to'g'ri xonaga (servisga) yo'naltirish."* |
| 5–20 | **Yangi mavzu** | Reverse proxy (mehmonxona resepsiyasi analogiyasi). Konfiguratsiya tuzilishi. `location` bloklari |
| 20–55 | **Amaliyot** | `amaliy-topshiriq.md`: MVP'ni Nginx ortiga qo'yish |
| 55–72 | **Challenge** | `challenge.md`: "502 detektivi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Nginx ishlaydi +10 · Reverse proxy +10 · SPA + API birga +20 · Challenge +20/+10/+5
