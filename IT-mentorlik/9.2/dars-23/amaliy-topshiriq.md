# 23-dars amaliy topshiriq

Namuna: `kod/api_bot.py`

## 🟢 Oson (+5 XP)
`/kurs` — Markaziy bank API'dan USD, EUR, RUB kurslari. Server javob bermasa, bot qulamasin.

## 🟡 O'rta (+10 XP)
- `/kurs 100 USD` — konvertatsiya (`CommandObject.args`)
- `/havo` — open-meteo'dan harorat
- `/shahar` — inline tugmalar bilan shahar tanlash, tanlov `sozlamalar.json` da saqlanadi

## 🔴 Qiyin (+20 XP)
- Kurslar keshlanadi (30 daqiqa)
- `/lugat hello` — inglizcha so'z ma'nosi (api.dictionaryapi.dev), talaffuz audio bo'lsa, `answer_audio` bilan yuboriladi
- Har kuni soat 08:00 da obuna bo'lganlarga ob-havo (aiogram'da `asyncio` task yoki `apscheduler` bilan)
