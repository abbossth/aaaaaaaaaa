# 20-dars amaliy topshiriq: birinchi bot

## Tayyorgarlik (mentor bilan birga)
```bash
mkdir telegram-bot && cd telegram-bot
python -m venv .venv
.venv\Scripts\activate            # Windows (Linux/Mac: source .venv/bin/activate)
pip install aiogram python-dotenv
```
1. @BotFather → `/newbot` → token oling.
2. `.env` fayli: `BOT_TOKEN=...` (namuna: `kod/.env.example`). `.gitignore` ga `.env` ni qo'shing!
3. `kod/bot.py` ni ishga tushiring: `python bot.py` → Telegram'da botingizga `/start` yozing 🎉

## 🟢 Oson (+10 XP)
Bot ishlaydi: `/start` ismingiz bilan salomlashadi, `/help` buyruqlar ro'yxatini beradi, matnni qaytaradi.

## 🟡 O'rta (+10 XP)
- `/vaqt` — hozirgi sana va vaqt (`datetime`)
- `/random` — 1–100 oralig'ida tasodifiy son
- Echo o'rniga: matn teskari yozib qaytarilsin, yonida harflar soni bilan
- BotFather'da `/setcommands` bilan buyruqlar menyusini sozlang

## 🔴 Qiyin (+20 XP)
- `/kalk 12 * 7` — kalkulyator (`eval` ISHLATMANG! 12-darsni eslang — `split` va `match` bilan)
- "salom", "rahmat", "qalaysan" kabi so'zlarga turli javoblar (`F.text.lower().in_(...)` yoki lug'at bilan)
- Rasm yuborilsa: "Chiroyli rasm! 📸 O'lchami: 1280x720" (`message.photo[-1].width/height`)
