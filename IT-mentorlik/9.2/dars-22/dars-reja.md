# 22-dars. FSM: holatlar, anketa ssenariysi

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Aiogram... foydalanuvchi ma'lumotlarini boshqarish"

## Maqsad
- Chekli avtomat (FSM — Finite State Machine) tushunchasini tushunadi: bot "hozir nimani kutayotganini" eslab qoladi.
- Aiogram'da `StatesGroup`, `State`, `FSMContext` bilan ishlaydi: `set_state`, `update_data`, `get_data`, `clear`.
- Bosqichma-bosqich ma'lumot yig'uvchi (anketa) bot yozadi: ism → yosh → telefon (kontakt tugmasi) → tasdiqlash.
- Har bir bosqichda validatsiya qiladi va "Bekor qilish" imkoniyatini beradi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Svetofor: qizil → sariq → yashil → ... Har bir holatda faqat ma'lum narsa bo'lishi mumkin. *"Bot ham shunday: 'ism kutyapman' holatida faqat ismni qabul qiladi."* |
| 5–10 | **Takrorlash** | 21-dars testi |
| 10–25 | **Yangi mavzu** | FSM diagrammasi (doskada). StatesGroup. FSMContext. Validatsiya. /cancel. Kontakt so'rash tugmasi |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md`: "IT to'garagiga ro'yxatdan o'tish" boti |
| 55–72 | **Challenge** | `challenge.md`: "Pitsa buyurtmasi" FSM |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
