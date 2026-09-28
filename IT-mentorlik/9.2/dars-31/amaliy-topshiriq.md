# 31-dars amaliy topshiriq

Asos: `maktab` bazasi. Avval uni qayta yarating: `\i ../dars-29/kod/maktab_schema.sql` → `\i ../dars-30/kod/maktab_data.sql`.

## 🟢 Oson (+5 XP)
1. `kod/constraints.sql` ni ishga tushiring. `\d baholar` bilan constraint'larni ko'ring.
2. `oqituvchilar` jadvaliga `email VARCHAR(100) UNIQUE` ustunini qo'shing.

## 🟡 O'rta (+10 XP)
3. `togaraklar` jadvaliga `max_azo INTEGER DEFAULT 15 CHECK (max_azo > 0)` qo'shing.
4. `sinflar.rahbar_id` uchun FK'ni `ON DELETE SET NULL` ga o'zgartiring (eski FK'ni `DROP CONSTRAINT`, yangisini `ADD`). Constraint nomini `\d sinflar` dan oling.

## 🔴 Qiyin (+20 XP)
5. "Kutubxona" bazasini noldan loyihalang: `kitoblar`, `oquvchilar`, `ijaralar`. Kamida: 1 ta ko'p ustunli UNIQUE, 2 ta CHECK (masalan, `qaytarish_sanasi >= olingan_sana`), FK'lar `CASCADE`/`RESTRICT` bilan. Har bir constraint'ni buzuvchi `INSERT` yozib, xatoni ko'rsating.
