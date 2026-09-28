# 33-dars slaydlari: Birinchi Telegram bot 🤖

## 1-slayd
📱 **Bugun sizning botingiz tug'iladi!**

## 2-slayd — Bot qanday ishlaydi?
```
Siz (📱) → Telegram serveri ☁️ ← (so'raydi: "yangi xabar bormi?") ← Bizning Python kod 💻
                                 → (javob yuboradi)                  →
```
Bu usul — **polling** (doim so'rab turish)

## 3-slayd — BotFather
1. @BotFather → `/newbot`
2. Ism: `Aziz Yordamchi` · Username: `aziz_8_2_bot` (oxiri `bot` bilan tugashi shart)
3. **Token:** `7012345678:AAH...` — bu botning **paroli** 🔐

## 4-slayd — ⚠️ Token xavfsizligi
❌ Kodga yozmang · ❌ GitHub'ga yuklamang · ✅ `.env` faylida saqlang + `.gitignore`
```
# .env
BOT_TOKEN=7012345678:AAH...
```

## 5-slayd — O'rnatish
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install aiogram python-dotenv
```

## 6-slayd — Handler = "agar ... bo'lsa, shunday javob ber"
```python
@dp.message(CommandStart())          # /start kelsa
async def start(message: Message):
    await message.answer("Salom! 👋")

@dp.message(F.text)                   # istalgan matn kelsa
async def echo(message: Message):
    await message.answer(message.text)
```
`async/await` — bot bir vaqtda **ko'p odamga** javob bera olishi uchun

## 7-slayd — Ishga tushirish
```python
async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

asyncio.run(main())
```
`python bot.py` → Telegram'da botga `/start` yozing 🎉
