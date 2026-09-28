# 34-dars. Telegram bot: komandalar, reply va inline keyboard, callback

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- Reply keyboard (pastdagi katta tugmalar) va inline keyboard (xabar ostidagi tugmalar) farqini biladi.
- `ReplyKeyboardBuilder`, `InlineKeyboardBuilder`, `adjust()` bilan tugmalar yasaydi.
- `callback_data` va `@dp.callback_query(F.data == ...)` bilan tugma bosilishini ushlaydi, `callback.answer()` qiladi.
- Xabarni tahrirlaydi (`edit_text`, `edit_reply_markup`).
- **Natija:** menyuli "Oshxona" boti va viktorina bot.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Telegram'da mashhur botni (masalan, Evos yoki Uzum bot) ochib ko'rsatish: *"Hamma narsa tugmalar bilan. Bugun shunday bot yasaymiz!"* |
| 5–10 | **Takrorlash** | 33-dars: lug'at bot uyga vazifasi, test |
| 10–25 | **Yangi mavzu** | `taqdimot.md`: reply vs inline, callback oqimi |
| 25–52 | **Jonli + amaliyot** | `kod/oshxona_bot.py` ni birga tahlil qilish → ishga tushirish → `amaliy-topshiriq.md` |
| 52–72 | **Challenge** | `challenge.md`: "Viktorina bot" |
| 72–80 | **Yakun** | Bir-birining viktorinasini o'ynash, XP |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge: ishlaydigan viktorina +15, eng qiziq savollar +10
