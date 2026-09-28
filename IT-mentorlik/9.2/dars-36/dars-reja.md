# 36-dars. 🚀 Mini loyiha: Telegram bot + PostgreSQL (asyncpg)

**Guruh:** 9.2 / 9.3 | **Turi:** 🚀 Loyiha | **Davomiyligi:** 80 daqiqa

## Maqsad
- Botni JSON fayl o'rniga PostgreSQL'ga ulaydi: `asyncpg` pool, `fetch`, `fetchrow`, `fetchval`, `execute`.
- SQL injection xavfini tushunadi va **faqat parametrli so'rovlar** (`$1, $2`) yozadi.
- UPSERT (`ON CONFLICT ... DO UPDATE`), `RETURNING`, tranzaksiya (`async with conn.transaction()`).
- Kodni qatlamlarga ajratadi: `bot.py` (Telegram) ↔ `db.py` (baza) ↔ `schema.sql`.
- **Natija:** jamoaviy bazali bot (namuna: "Kutubxona bot").

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 22-darsdagi anketa botini qayta ishga tushiramiz → `royxat.json` ... 2 kishi bir vaqtda yozsa, fayl buziladi 💥. *"Real botlar bazasiz yashamaydi"* |
| 5–20 | **Yangi mavzu** | `taqdimot.md`: asyncpg, parametrli so'rov, SQL injection (jonli namoyish), tranzaksiya |
| 20–30 | **Namuna tahlili** | `kod/`: `schema.sql` → `db.py` → `sinov.py` → `bot.py` |
| 30–72 | **Jamoaviy loyiha** | `amaliy-topshiriq.md`: 3 kishilik jamoalar o'z bazali botini quradi |
| 72–80 | **Demo** | Har jamoa 1 daqiqa: bot + `SELECT` bilan bazadagi ma'lumot |

## Baholash (XP)
- Ishlaydigan bazali bot +30 · Tranzaksiya ishlatilgan +10 · Statistika (GROUP BY) +10 · Eng yaxshi demo +20
