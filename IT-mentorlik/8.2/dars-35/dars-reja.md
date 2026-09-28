# 35-dars. FSM: bosqichma-bosqich ma'lumot yig'ish — anketa boti

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- FSM (Finite State Machine — chekli holatlar mashinasi) g'oyasini tushunadi: bot "qaysi savolda turganini" eslab qoladi.
- `StatesGroup`, `State`, `FSMContext`: `set_state`, `update_data`, `get_data`, `clear`.
- Har bir qadamda validatsiya qiladi (yosh — son, telefon — format) va xato bo'lsa o'sha qadamda qoladi.
- `/cancel` bilan jarayonni bekor qiladi. Kontakt tugmasi (`request_contact=True`).
- **Natija:** to'garakka yozilish anketa boti, ma'lumotlar JSON faylga saqlanadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Rol o'yini: mentor = bot, o'quvchi = foydalanuvchi. Mentor "Ismingiz?" deydi, o'quvchi "Pitsa!" deydi 😄 *"Bot qaysi savol berganini qanday eslab qoladi?"* |
| 5–10 | **Takrorlash** | 34-dars: viktorina natijalari, test |
| 10–25 | **Yangi mavzu** | `taqdimot.md`: holatlar diagrammasi (doskada chizish), FSM kodi |
| 25–52 | **Jonli + amaliyot** | `kod/royxat_bot.py` tahlili → ishga tushirish → `amaliy-topshiriq.md` |
| 52–74 | **Challenge** | `challenge.md`: "Pitsa buyurtmasi" 🍕 |
| 74–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge: ishlaydigan birinchi 3 juftlik +30/+20/+10
