# 30-dars. CRUD: INSERT, SELECT, UPDATE, DELETE

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 3-bob, "CRUD amallarni (create, read, update, delete) bajarish"

## Maqsad
- CRUD tushunchasini biladi va har bir amalni SQL'da bajaradi: `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- `SELECT` asoslari: ustunlarni tanlash, `WHERE`, `ORDER BY`, `LIMIT`, `AS` (taxallus).
- `UPDATE`/`DELETE` da `WHERE` ni **unutish xavfini** tushunadi va tranzaksiya (`BEGIN`/`ROLLBACK`) bilan o'zini himoya qiladi.
- `RETURNING` bilan yangi yaratilgan/o'zgargan yozuvni qaytaradi.
- Botning CRUD amallarini (ro'yxatdan o'tish, profil o'zgartirish, o'chirish) SQL'da ifodalay oladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Real hikoya: dasturchi `WHERE` ni unutib `UPDATE users SET password = '123'` qilgan... 😱 *"Bugun SQL'ning 4 ta asosiy buyrug'ini va o'zingizni qanday himoya qilishni o'rganamiz."* |
| 5–10 | **Takrorlash** | 29-dars testi. `maktab_data.sql` ni yuklash |
| 10–28 | **Yangi mavzu** | CRUD ↔ SQL ↔ HTTP ↔ bot jadvali. Har bir buyruq jonli |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "SQL quiz poygasi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
