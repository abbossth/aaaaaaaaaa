# 30-dars slaydlari: CRUD 🔁

## 1-slayd
`UPDATE users SET password = '123';` — **WHERE qani?!** 😱

## 2-slayd — CRUD
| Amal | SQL | HTTP | Botda |
|---|---|---|---|
| **C**reate | `INSERT` | POST | /register |
| **R**ead | `SELECT` | GET | /profil |
| **U**pdate | `UPDATE` | PUT/PATCH | ismni o'zgartirish |
| **D**elete | `DELETE` | DELETE | /delete_me |

## 3-slayd — INSERT
```sql
INSERT INTO talabalar (ism, sinf_id) VALUES ('Ali Valiyev', 1);
INSERT INTO talabalar (ism, sinf_id) VALUES ('A', 1), ('B', 2);   -- bir nechta
INSERT INTO talabalar (ism) VALUES ('Yangi') RETURNING id;      -- yangi id'ni qaytaradi
```

## 4-slayd — SELECT
```sql
SELECT * FROM talabalar;
SELECT ism, tugilgan_sana FROM talabalar WHERE sinf_id = 1;
SELECT ism AS "Ism" FROM talabalar ORDER BY ism LIMIT 5;
```

## 5-slayd — UPDATE va DELETE
```sql
UPDATE talabalar SET sinf_id = 2 WHERE id = 3;
DELETE FROM talabalar WHERE id = 10;
```
⚠️ **WHERE siz — HAMMA qatorlar!**

## 6-slayd — Xavfsizlik kamari: tranzaksiya 🪢
```sql
BEGIN;
UPDATE talabalar SET sinf_id = 2 WHERE ...;
SELECT * FROM talabalar;     -- tekshirish
ROLLBACK;                    -- ❌ bekor qilish   (yoki COMMIT; ✅ saqlash)
```
**Qoida:** avval `SELECT ... WHERE`, keyin xuddi shu `WHERE` bilan `UPDATE/DELETE`
