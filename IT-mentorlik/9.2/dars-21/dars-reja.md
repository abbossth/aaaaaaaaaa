# 21-dars. Reply va inline keyboard, callback query

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Aiogram... Inline keyboard va reply keyboard"

## Maqsad
- Reply keyboard (pastdagi tugmalar) va inline keyboard (xabar ostidagi tugmalar) farqini biladi.
- `ReplyKeyboardBuilder` va `InlineKeyboardBuilder` bilan tugmalar yaratadi.
- `callback_data` va `@dp.callback_query(F.data == ...)` bilan inline tugma bosilishini ushlaydi. `callback.answer()` ni unutmaydi.
- Xabarni tahrirlash (`edit_text`) orqali "sahifalarni almashtirish" effektini yaratadi.
- `Router` bilan kodni fayllarga ajratadi.
- Menyuli bot va tugmali viktorina yaratadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Mashhur botlar: pastda "📍 Manzil", "🛒 Savat" tugmalari; xabar ostida "⬅️ ➡️" tugmalari. *"Buyruq yozish noqulay. Tugmalar — botning interfeysi."* |
| 5–10 | **Takrorlash** | 20-dars testi |
| 10–25 | **Yangi mavzu** | Reply vs inline. Builder'lar. callback_data. `callback.answer()`. `edit_text`. Router |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md`: "Maktab oshxonasi" boti |
| 55–72 | **Challenge** | `challenge.md`: "Tugmali viktorina" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
