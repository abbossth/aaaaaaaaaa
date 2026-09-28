# 35-dars slaydlari: FSM 📋

## 1-slayd
🤖 "Ismingiz?" — 👦 "Pitsa!" — 🤖 "Yoshingiz?" — 👦 "Salom" 😵

## 2-slayd — FSM = holatlar zanjiri
```
/register → [ism] → [yosh] → [yo'nalish] → [telefon] → [tasdiq] → ✅ saqlandi
              ↑ xato bo'lsa — o'sha holatda qoladi
```
Har bir foydalanuvchining **o'z** holati bor

## 3-slayd — Holatlarni e'lon qilish
```python
from aiogram.fsm.state import State, StatesGroup

class Royxat(StatesGroup):
    ism = State()
    yosh = State()
    telefon = State()
```

## 4-slayd — Holatga o'tish va ma'lumot saqlash
```python
@dp.message(Command("register"))
async def boshla(message: Message, state: FSMContext):
    await state.set_state(Royxat.ism)
    await message.answer("Ismingiz?")

@dp.message(Royxat.ism)                         # faqat shu holatda ishlaydi!
async def ism_ol(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Royxat.yosh)
    await message.answer("Yoshingiz?")
```

## 5-slayd — Validatsiya
```python
@dp.message(Royxat.yosh)
async def yosh_ol(message: Message, state: FSMContext):
    if not message.text.isdigit() or not 10 <= int(message.text) <= 18:
        return await message.answer("❗ 10–18 oralig'ida son kiriting")   # holat o'zgarmaydi
    ...
```

## 6-slayd — Yakunlash
```python
data = await state.get_data()     # {"ism": "Aziz", "yosh": 14, ...}
await state.clear()               # holatdan chiqish
```

## 7-slayd — Kontakt tugmasi 📱
```python
kb.button(text="📱 Raqamni yuborish", request_contact=True)
# ushlash: @dp.message(Royxat.telefon, F.contact) → message.contact.phone_number
```
