# 22-dars amaliy topshiriq: ro'yxatdan o'tish boti 📝

Namuna: `kod/royxat_bot.py` (avval o'zingiz urinib ko'ring!)

## 🟢 Oson (+5 XP)
`/register` → ism → yosh → "Rahmat, {ism}! Siz {yosh} yoshdasiz" (FSM bilan, 2 ta holat).

## 🟡 O'rta (+10 XP)
- Validatsiya: ism (3+ harf, raqamsiz), yosh (10..18 son). Noto'g'ri bo'lsa, holat o'zgarmaydi, qayta so'raladi.
- Telefon — **kontakt tugmasi** orqali.
- `/cancel` istalgan bosqichda ishlaydi.
- Oxirida: ma'lumotlarni ko'rsatib, "✅ Tasdiqlash / 🔁 Qaytadan" inline tugmalari.

## 🔴 Qiyin (+20 XP)
- Tasdiqlangan ro'yxat `royxat.json` ga saqlansin.
- Bir foydalanuvchi 2 marta ro'yxatdan o'ta olmasin (`user_id` bo'yicha tekshirish).
- Admin (sizning `ADMIN_ID`) uchun `/list` buyrug'i: barcha ro'yxatdan o'tganlar.
- Yangi ro'yxatdan o'tgan haqida admin'ga avtomatik xabar.
