# 20-dars. Aiogram 3: BotFather, echo bot, /start, /help

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Aiogram kutubxonasi yordamida telegram bot dasturini tuzish"

## Maqsad
- Telegram bot qanday ishlashini tushunadi: Bot API, token, polling (long polling) va webhook farqi.
- @BotFather orqali bot yaratadi va token oladi. Tokenni xavfsiz saqlaydi (`.env`).
- Aiogram 3 tuzilishini biladi: `Bot`, `Dispatcher`, `Router`, handler'lar, filtrlar (`CommandStart`, `Command`, `F.text`).
- Asinxron (`async/await`) handler'lar yozadi. (Chuqur asinxronlik — 38-darsda.)
- `/start`, `/help` komandalari va echo bot yaratadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Oraliq nazorat natijalari (5 daqiqa). Keyin: *"Telegram'da qancha bot ishlatasiz? @uzbek_translator_bot, ob-havo, musiqa... Bugun dars oxirida SIZNING botingiz telefoningizda javob beradi!"* |
| 5–15 | **Nazorat tahlili** | Eng ko'p uchragan 3 xato |
| 15–28 | **Yangi mavzu** | Bot API sxemasi (foydalanuvchi → Telegram serveri → sizning kodingiz). Polling vs webhook. BotFather. Token xavfsizligi. Aiogram tuzilishi |
| 28–60 | **Jonli + amaliyot** | BotFather → venv → `pip install aiogram python-dotenv` → `kod/bot.py` → ishga tushirish → telefonda sinash 📱 |
| 60–75 | **Challenge** | `challenge.md`: "Bot shaxsiyati" |
| 75–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Bot ishlaydi +10 · /start va /help +5 · Challenge +20/+10/+5
