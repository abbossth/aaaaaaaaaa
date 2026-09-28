# 21-dars amaliy topshiriq: "Maktab oshxonasi" boti 🍽

Namuna: `kod/oshxona_bot.py` (avval o'zingiz urinib ko'ring!)

## 🟢 Oson (+5 XP)
Reply keyboard: "🍽 Menyu", "📞 Aloqa", "ℹ️ Biz haqimizda". Har biri o'z javobini beradi.

## 🟡 O'rta (+10 XP)
- "🍽 Menyu" bosilganda: inline tugmalar bilan taomlar ro'yxati.
- Taom bosilganda: savatga qo'shiladi va `callback.answer("Qo'shildi ✅")` qalqib chiqadi.
- "🛒 Savat" — tanlanganlar va jami summa.

## 🔴 Qiyin (+20 XP)
- Savatda har bir taom yonida ➕ ➖ tugmalari (`edit_text` bilan xabar yangilanadi).
- Kodni `Router`lar bilan fayllarga ajrating: `handlers/start.py`, `handlers/menu.py`, `keyboards.py`, `main.py`.
- "✅ Buyurtma berish" → buyurtma matni admin'ga (o'zingizning chat ID'ingizga) yuborilsin: `bot.send_message(ADMIN_ID, ...)`.
