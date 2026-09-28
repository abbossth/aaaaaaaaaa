# 31-dars slaydlari: Bazaning qo'riqchilari 🛡

## 1-slayd
😱 `baho = 7` · `yosh = -3` · `telefon = 'salom'` — kim ruxsat berdi?

## 2-slayd — Constraint turlari
| Constraint | Qo'riqlaydi | Misol |
|---|---|---|
| `PRIMARY KEY` | Har bir qator noyob va bo'sh emas | `id SERIAL PRIMARY KEY` |
| `FOREIGN KEY` | Bog'lanish haqiqiy bo'lsin | `sinf_id INTEGER REFERENCES sinflar(id)` |
| `UNIQUE` | Takrorlanmasin | `telegram_id BIGINT UNIQUE` |
| `NOT NULL` | Bo'sh bo'lmasin | `ism VARCHAR(100) NOT NULL` |
| `CHECK` | Shartga mos bo'lsin | `CHECK (baho BETWEEN 1 AND 5)` |
| `DEFAULT` | Qiymat berilmasa | `faol BOOLEAN DEFAULT true` |

## 3-slayd — FOREIGN KEY: ota o'chirilsa nima bo'ladi?
| Variant | Natija |
|---|---|
| `ON DELETE RESTRICT` (standart) | O'chirishga ruxsat bermaydi ❌ |
| `ON DELETE CASCADE` | Bog'liq qatorlar ham o'chadi 🗑 |
| `ON DELETE SET NULL` | Bog'liq ustun `NULL` bo'ladi |

Talaba o'chsa → baholari ham o'chsin (`CASCADE`). Sinf rahbari ishdan ketsa → sinf o'chmasin (`SET NULL`).

## 4-slayd — Ko'p ustunli UNIQUE
```sql
ALTER TABLE baholar ADD CONSTRAINT bir_kunda_bir_baho
    UNIQUE (talaba_id, fan, sana);
```

## 5-slayd — ALTER TABLE shpargalka
```sql
ALTER TABLE t ADD COLUMN c TYPE;             -- ustun qo'shish
ALTER TABLE t DROP COLUMN c;                 -- o'chirish
ALTER TABLE t RENAME COLUMN a TO b;          -- nomini o'zgartirish
ALTER TABLE t ALTER COLUMN c TYPE VARCHAR(100);
ALTER TABLE t ALTER COLUMN c SET NOT NULL;   -- / DROP NOT NULL
ALTER TABLE t ALTER COLUMN c SET DEFAULT 0;
ALTER TABLE t ADD CONSTRAINT nom CHECK (...);
ALTER TABLE t DROP CONSTRAINT nom;
```

## 6-slayd — ⚠️ Mavjud ma'lumot bilan
Jadvalda `baho = 7` bo'lsa, `ADD CONSTRAINT ... CHECK (baho <= 5)` **xato beradi**. Avval ma'lumotni tozalang!

## 7-slayd — Qoida
> Validatsiya **ikki joyda**: Python/FastAPI'da (foydalanuvchiga chiroyli xabar) va **bazada** (oxirgi himoya chizig'i).
