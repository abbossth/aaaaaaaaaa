# 22-dars slaydlari: FSM 🚦

## 1-slayd
**Bot "hozir nimani kutayotganini" qanday eslab qoladi?**

## 2-slayd — FSM diagrammasi
```
/register ──▶ [ism kutilmoqda] ──ism──▶ [yosh kutilmoqda] ──yosh──▶ [telefon kutilmoqda]
                                                                         │ kontakt
                  ◀──── /cancel (istalgan holatdan) ────            [tasdiqlash]
                                                                    ✅ saqlash → clear
```

## 3-slayd — Holatlar
```python
from aiogram.fsm.state import State, StatesGroup

class Royxat(StatesGroup):
    ism = State()
    yosh = State()
    telefon = State()
```

## 4-slayd — Holatni boshqarish
```python
@router.message(Command("register"))
async def boshla(message: Message, state: FSMContext):
    await state.set_state(Royxat.ism)
    await message.answer("Ismingiz?")

@router.message(Royxat.ism, F.text)
async def ism_ol(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Royxat.yosh)
    await message.answer("Yoshingiz?")
```

## 5-slayd — Ma'lumotni olish va tozalash
```python
data = await state.get_data()   # {"ism": "Aziz", "yosh": 15, ...}
await state.clear()             # holat va ma'lumotni tozalash
```

## 6-slayd — Kontakt tugmasi 📱
```python
kb = ReplyKeyboardBuilder()
kb.button(text="📱 Raqamni yuborish", request_contact=True)
...
@router.message(Royxat.telefon, F.contact)
async def tel(message: Message, state: FSMContext):
    raqam = message.contact.phone_number
```
