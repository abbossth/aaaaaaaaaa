# 36-dars. Bot + tashqi API: valyuta kursi va ob-havo boti

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- API nima ekanini eslaydi (20-dars, JS `fetch`) va Python'da `requests` bilan so'rov yuboradi.
- JSON javobni Python lug'at/ro'yxatiga aylantiradi va kerakli qismini oladi.
- Botda asinxron `aiohttp` bilan API chaqiradi (bot "qotib qolmasligi" uchun).
- Xatolarni ushlaydi: internet yo'q, API ishlamayapti, noto'g'ri valyuta kodi.
- **Natija:** `/kurs USD 100`, `/havo` buyruqlari ishlaydigan bot.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Dollar kursini har kuni bank saytiga kirib qaraysizmi? Bot 1 soniyada aytadi!"* |
| 5–10 | **Takrorlash** | 35-dars: FSM, pitsa boti natijalari |
| 10–25 | **Yangi mavzu** | `taqdimot.md` + `kod/api_sinov.py` (brauzerda API havolasini ochib JSON'ni ko'rish) |
| 25–52 | **Jonli + amaliyot** | `kod/api_bot.py` tahlili → `amaliy-topshiriq.md` |
| 52–72 | **Challenge** | `challenge.md`: "API ovchisi" 🏹 |
| 72–80 | **Yakun** | Ovoz berish, XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge 🥇 +20 · 🥈 +10 · 🥉 +5
