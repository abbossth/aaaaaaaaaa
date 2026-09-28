# 34-dars mentor eslatmasi

- Batafsil material: `../../9.2/dars-21/` (taqdimot, test, mentor eslatmalari).
- `kod/quiz_bot.py` — faqat 8.2 uchun yozilgan (aiogram 3 bilan import tekshirilgan). Holat xotirada (`dict`) saqlanadi — bot qayta ishga tushsa natijalar yo'qoladi. Bu 38–43-darslardagi PostgreSQL'ga ko'prik.
- Eng ko'p xato: reply tugma matni va `F.text == "..."` dagi matn emoji bilan **aynan** bir xil bo'lmasa handler ishlamaydi.
- Ikkita o'quvchi bitta token ishlatsa — `TelegramConflictError`. Har kim o'z botini ishlatsin.
