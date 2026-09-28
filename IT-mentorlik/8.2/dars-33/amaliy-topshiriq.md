# 33-dars amaliy topshiriq

Asos: `kod/bot.py` (`.env.example` ni `.env` ga nusxalab, tokeningizni yozing)

## 🟢 Oson (+5 XP)
1. `/start` javobini o'zgartiring: foydalanuvchi ismi + emoji + 3 qatorli tanishtiruv.
2. `/about` — o'zingiz haqida ma'lumot.

## 🟡 O'rta (+10 XP)
3. Echo o'rniga "aqlli" javob: `salom` → "Va alaykum assalom! 😊", `qalaysan` → "Zo'r, o'zingchi?", boshqasi → echo.
4. `/time` — hozirgi vaqtni chiqaradi (`datetime.now().strftime("%H:%M")`).

## 🔴 Qiyin (+20 XP)
5. Foydalanuvchi son yuborsa → uning kvadratini, matn yuborsa → teskarisini (`[::-1]`) qaytaring.
6. `/zar` — tasodifiy son 1–6 (`random.randint`) yoki Telegram'ning 🎲 animatsiyasi: `await message.answer_dice()`.
