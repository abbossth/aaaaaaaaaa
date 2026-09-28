# 21-dars slaydlari: Tugmalar ⌨️

## 1-slayd
**Buyruq yozish noqulay → tugmalar!**

## 2-slayd — 2 xil klaviatura
⌨️ **Reply keyboard:** yozish maydoni o'rnida. Bosilsa → oddiy matn xabar yuboriladi
🔘 **Inline keyboard:** xabar ostida. Bosilsa → `callback_query` (xabar yuborilmaydi)

## 3-slayd — Reply keyboard
```python
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb = ReplyKeyboardBuilder()
kb.button(text="🍽 Menyu")
kb.button(text="📞 Aloqa")
kb.adjust(2)   # qatorda 2 ta
await message.answer("Tanlang:", reply_markup=kb.as_markup(resize_keyboard=True))

@dp.message(F.text == "🍽 Menyu")
async def menyu(message: Message): ...
```

## 4-slayd — Inline keyboard
```python
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = InlineKeyboardBuilder()
kb.button(text="✅ Ha", callback_data="javob:ha")
kb.button(text="❌ Yo'q", callback_data="javob:yoq")
await message.answer("Davom etamizmi?", reply_markup=kb.as_markup())
```

## 5-slayd — Callback'ni ushlash
```python
@dp.callback_query(F.data.startswith("javob:"))
async def javob(callback: CallbackQuery):
    tanlov = callback.data.split(":")[1]
    await callback.message.edit_text(f"Siz tanladingiz: {tanlov}")
    await callback.answer()   # ⏳ "soat" belgisini o'chiradi — UNUTMANG!
```

## 6-slayd — Router: kodni tartiblash
```
bot/
├── main.py         # Bot, Dispatcher, include_router
├── handlers/
│   ├── start.py    # router = Router()
│   └── menu.py
└── keyboards.py
```
