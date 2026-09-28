# 30-dars amaliy topshiriq

Avval: `\i maktab_schema.sql` → `\i maktab_data.sql` (`kod/` papkasidan; sxema `../dars-29/kod/` da).

## 🟢 Oson (+5 XP): READ
1. Barcha talabalar
2. Faqat ismlar va tug'ilgan sanalar, ism bo'yicha alifbo tartibida
3. `sinf_id = 1` bo'lgan talabalar
4. Eng yosh 3 ta talaba (`ORDER BY tugilgan_sana DESC LIMIT 3`)

## 🟡 O'rta (+10 XP): CREATE / UPDATE / DELETE
5. O'zingizni `talabalar` ga qo'shing (`RETURNING id` bilan).
6. O'zingizga 3 ta baho qo'shing (bitta `INSERT` da).
7. O'z ismingizni o'zgartiring.
8. Telegram ID'si yo'q talabalar (`WHERE telegram_id IS NULL`).
9. `BEGIN` → barcha talabalarni o'chiring (`DELETE FROM talabalar;`) → `SELECT count(*)` → `ROLLBACK` → yana `SELECT count(*)`. Nima bo'ldi? 😅

## 🔴 Qiyin (+20 XP)
10. Bot loyihangiz jadvallariga (`bot_schema.sql`) namuna ma'lumotlar qo'shing (har jadvalga 5+ qator).
11. Botingizning har bir buyrug'i uchun mos SQL so'rovni yozing (`bot_sorovlar.sql`): masalan, `/start` → foydalanuvchi mavjudligini tekshirish va yo'q bo'lsa `INSERT`.
