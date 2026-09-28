# 32-dars challenge: "Eng kichik image" 🪶

**Vaqt:** 14 daqiqa | **Format:** jamoalar

Vazifa: MVP serveringiz image'ini **iloji boricha kichik** qiling. Shartlar:
- `curl localhost:3000/api/health` → `{"status":"ok",...}` ishlashi **shart**.
- `USER` root bo'lmasin.

G'oyalar: `-alpine` asos · `--omit=dev` · `.dockerignore` · `npm cache clean --force` · multi-stage · `node:20-alpine` o'rniga `gcr.io/distroless/nodejs20-debian12` 😈

**Hakamlik:** `docker images` dagi SIZE. Mentor ishlashini tekshiradi.
**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5 · 100 MB dan kichik har bir jamoa +5
