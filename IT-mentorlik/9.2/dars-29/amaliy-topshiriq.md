# 29-dars amaliy topshiriq: "maktab" bazasi 🏫

## 🟢 Oson (+5 XP)
1. psql yoki pgAdmin orqali ulaning. `SELECT version();` natijasini ko'ring.
2. `CREATE DATABASE maktab;` → `\c maktab`.
3. `sinflar` va `talabalar` jadvallarini qo'lda yozing (taqdimotdagidek). `\dt` va `\d talabalar` bilan tekshiring.

## 🟡 O'rta (+10 XP)
4. `kod/maktab_schema.sql` ni ishga tushiring (`\i` yoki pgAdmin Query Tool). Nechta jadval yaratildi?
5. pgAdmin'da: Schemas → Tables → jadval ustida o'ng tugma → **ERD For Table** — diagramma paydo bo'ladimi?

## 🔴 Qiyin (+20 XP)
6. 28-darsdagi **o'z bot loyihangiz** ER-diagrammasi bo'yicha `CREATE TABLE` skriptini yozing (`bot_schema.sql`). Turlarni to'g'ri tanlang: telegram_id uchun `BIGINT`, pul uchun `NUMERIC`!
7. `ALTER TABLE` bilan `talabalar` ga `email VARCHAR(100)` ustunini qo'shing (31-darsda chuqurroq).
