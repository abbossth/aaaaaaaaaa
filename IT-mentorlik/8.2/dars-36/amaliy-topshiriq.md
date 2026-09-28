# 36-dars amaliy topshiriq

Asos: `kod/api_sinov.py` (oddiy Python), `kod/api_bot.py` (bot, 9.2 bilan umumiy). O'rnatish: `pip install requests aiohttp`.

## 🟢 Oson (+5 XP)
1. `api_sinov.py` ni ishga tushiring. Kazakistan tengesi (KZT) va Xitoy yuani (CNY) kursini ham chiqaring.
2. O'z shahringiz koordinatalarini (Google Maps'dan) qo'yib, ob-havoni oling.

## 🟡 O'rta (+10 XP)
3. Botda `/kurs 100 USD` → "100 USD = 1 265 050 so'm". Noto'g'ri valyuta kodi bo'lsa — mavjud kodlar ro'yxati.
4. `/havo` javobiga ob-havo belgisini qo'shing: harorat < 0 → 🥶, 0–15 → 🧥, 15–25 → 😊, > 25 → 🥵.

## 🔴 Qiyin (+20 XP)
5. `/ertaga` — ertangi kunning eng yuqori/eng past harorati (`daily=temperature_2m_max,temperature_2m_min`).
6. So'm → valyuta teskari hisoblash: `/som 1000000 EUR`.
