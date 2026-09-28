# 29-dars challenge: "Tur tanlash" 🎯

**Vaqt:** 12 daqiqa | **Format:** jamoalar

Har bir maydon uchun eng to'g'ri PostgreSQL turini tanlang (+1) va nega ekanini ayting (+1):

| № | Maydon | Javob |
|---|---|---|
| 1 | Telegram foydalanuvchi ID'si (masalan, 5234567890) | `BIGINT` (INTEGER maks. ~2.1 mlrd) |
| 2 | Mahsulot narxi (so'm, tiyinlar bilan) | `NUMERIC(12,2)` (float emas — yaxlitlash xatolari!) |
| 3 | Tug'ilgan sana | `DATE` |
| 4 | Buyurtma yaratilgan vaqt | `TIMESTAMP` (yoki `TIMESTAMPTZ`) |
| 5 | Telefon raqami (+998901234567) | `VARCHAR(15)` (son emas! boshida `+`, 0 bo'lishi mumkin, hisob-kitob qilinmaydi) |
| 6 | Blog post matni | `TEXT` |
| 7 | "Faol foydalanuvchimi?" | `BOOLEAN` |
| 8 | Baho (2–5) | `SMALLINT` (+ CHECK, 31-dars) |
| 9 | Pochta indeksi (100100) | `VARCHAR(6)` |
| 10 | Avtomatik o'suvchi ID | `SERIAL` / `GENERATED ALWAYS AS IDENTITY` |

**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
