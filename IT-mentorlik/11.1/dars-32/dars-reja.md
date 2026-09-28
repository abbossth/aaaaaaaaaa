# 32-dars. Dockerfile: Node ilovani konteynerlash, build/tag/push, kesh

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "Dockerfile yozish va image yaratish"

## Maqsad
- Dockerfile buyruqlarini biladi: `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `EXPOSE`, `USER`, `HEALTHCHECK`, `CMD`.
- Qatlam keshini tushunadi va Dockerfile'ni kesh uchun to'g'ri tartibda yozadi (avval `package.json`, keyin kod).
- `.dockerignore` bilan keraksiz/maxfiy fayllarni image'ga kiritmaydi.
- `docker build`, `docker tag` (semver), `docker push` bilan Docker Hub'ga image yuklaydi.
- Multi-stage build g'oyasini biladi (React frontend uchun).
- **Jamoa natijasi:** MVP serveri Docker Hub'da, istalgan kompyuterda 1 buyruq bilan ishga tushadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Mentor sinfdoshining noutbukida `docker run <login>/mvp-server` — Node o'rnatilmagan kompyuterda ilova ishlaydi 🤯 |
| 5–10 | **Takrorlash** | Docker Quest natijalari, 31-dars testi |
| 10–28 | **Yangi mavzu** | `taqdimot.md`: Dockerfile anatomiyasi, kesh, .dockerignore, tag'lar |
| 28–58 | **Jamoaviy amaliyot** | `amaliy-topshiriq.md`: har bir jamoa o'z MVP serverini konteynerlaydi va push qiladi |
| 58–72 | **Challenge** | `challenge.md`: "Eng kichik image" musobaqasi |
| 72–80 | **Yakun** | Jamoalar image'larini almashib ishga tushiradi, XP |

## Baholash (XP)
- Ishlaydigan Dockerfile +10 · Docker Hub'da image +10 · Amaliyot +5/+10/+20 · Challenge 🥇 +20
