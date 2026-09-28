# 20-dars. fetch va API, async/await — ob-havo ilovasi

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- API nima ekanini va sayt serverdan qanday ma'lumot olishini tushunadi.
- Sinxron va asinxron kod farqini sodda misolda tushunadi (restoranda buyurtma kutish).
- `fetch` + `async/await` bilan JSON oladi. `try/catch` bilan xatolarni ushlaydi. `response.ok` ni tekshiradi.
- "Yuklanmoqda..." holatini va xato xabarini ko'rsatadi.
- Open-Meteo API (kalitsiz, bepul) bilan shahar ob-havosini ko'rsatuvchi ilova yaratadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Console'da: `fetch("https://api.github.com/users/torvalds").then(r => r.json()).then(console.log)`. *"Bitta qator bilan boshqa kompaniyaning serveridan ma'lumot oldik!"* |
| 5–10 | **Takrorlash** | 19-dars testi |
| 10–25 | **Yangi mavzu** | API, JSON, asinxronlik (restoran analogiyasi), Promise, async/await, try/catch, loading/error holatlari |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md`: ob-havo ilovasi |
| 55–72 | **Challenge** | `challenge.md`: "API safari" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Ob-havo ilovasi +5/+10/+20 · Challenge +20/+10/+5
