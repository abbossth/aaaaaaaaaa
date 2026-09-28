# 34-dars slaydlari: Tugmalar ⌨️

## 1-slayd
🍔 Evos, 🛒 Uzum — **hamma narsa tugmalarda**. Foydalanuvchi yozishni yoqtirmaydi!

## 2-slayd — 2 xil klaviatura
| Reply keyboard | Inline keyboard |
|---|---|
| Pastda, klaviatura o'rnida | Xabar ostida |
| Bosilsa → **oddiy matn** yuboriladi | Bosilsa → **callback** (ko'rinmas signal) |
| Ushlash: `F.text == "🍽 Menyu"` | Ushlash: `F.data == "savat"` |
| Asosiy menyu uchun | Tanlov, "Yoqdi 👍", sahifalash |

## 3-slayd — Reply keyboard
```python
kb = ReplyKeyboardBuilder()
kb.button(text="🍽 Menyu")
kb.button(text="🛒 Savat")
kb.button(text="📞 Aloqa")
kb.adjust(2, 1)          # 1-qatorda 2 ta, 2-qatorda 1 ta
await message.answer("Tanlang:", reply_markup=kb.as_markup(resize_keyboard=True))
```

## 4-slayd — Inline keyboard
```python
kb = InlineKeyboardBuilder()
kb.button(text="🍕 Pitsa — 65 000", callback_data="qosh:pitsa")
kb.button(text="🍔 Burger — 35 000", callback_data="qosh:burger")
kb.adjust(1)
```

## 5-slayd — Callback'ni ushlash
```python
@dp.callback_query(F.data.startswith("qosh:"))
async def qosh(callback: CallbackQuery):
    taom = callback.data.split(":")[1]      # "pitsa"
    await callback.answer("Savatga qo'shildi ✅")   # ⚠️ shart! aks holda soat ⏳ aylanib turadi
```

## 6-slayd — Xabarni tahrirlash ✏️
```python
await callback.message.edit_text("Yangi matn", reply_markup=yangi_kb)
```
Yangi xabar emas — **o'sha** xabar o'zgaradi (chat toza qoladi)

## 7-slayd — Qoidalar
- `callback_data` — **64 baytgacha**
- Har bir callback'ga `callback.answer()`
- `show_alert=True` → oynada chiqadigan xabar
