# 20-dars slaydlari: Telegram bot 🤖

## 1-slayd
📱 **Dars oxirida sizning botingiz javob beradi!**

## 2-slayd — Bot qanday ishlaydi?
```
Foydalanuvchi ──xabar──▶ Telegram serveri ◀──"Yangi xabar bormi?"── Sizning kodingiz (polling)
                                          ──────javob──────▶
```
**Polling:** kod o'zi so'rab turadi (o'rganish uchun oson)
**Webhook:** Telegram o'zi kodga yuboradi (production uchun, serverda)

## 3-slayd — BotFather 👴
`/newbot` → nom → username (`..._bot` bilan tugashi shart) → **TOKEN**
`1234567890:AAH...xyz` ← bu botingizning paroli!

## 4-slayd — ⚠️ Token xavfsizligi
❌ Kodga yozmang · ❌ GitHub'ga yuklamang · ❌ Hech kimga bermang
✅ `.env` fayl + `.gitignore`
Token oshkor bo'lsa: BotFather → `/revoke`

## 5-slayd — Aiogram 3 tuzilishi
```python
dp = Dispatcher()                    # "dispetcher": xabarni kerakli handler'ga yo'naltiradi

@dp.message(CommandStart())          # filtr: faqat /start
async def start(message: Message):   # handler
    await message.answer("Salom!")
```

## 6-slayd — Filtrlar
`CommandStart()` → /start · `Command("help")` → /help · `F.text` → har qanday matn
`F.photo` → rasm · `F.text == "salom"` → aniq matn · `F.text.contains("narx")`

## 7-slayd — async/await nima uchun?
Bot bir vaqtda minglab odam bilan gaplashadi. Bitta foydalanuvchini kutib, qolganlarini "muzlatib" qo'ymasligi uchun.
