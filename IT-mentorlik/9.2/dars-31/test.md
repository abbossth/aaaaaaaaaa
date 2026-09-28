# 31-dars tezkor test

1. Baho 1–5 oralig'ida bo'lishini qaysi constraint ta'minlaydi? — `CHECK (baho BETWEEN 1 AND 5)`
2. Ota qator o'chirilsa, bog'liq qatorlar ham o'chsin — ? — `ON DELETE CASCADE`
3. `FOREIGN KEY` ning standart xatti-harakati? — O'chirishga ruxsat bermaydi (RESTRICT/NO ACTION)
4. Mavjud jadvalga ustun qo'shish? — `ALTER TABLE t ADD COLUMN ...`
5. `UNIQUE (talaba_id, fan, sana)` nimani anglatadi? — Bu uch qiymatning **birikmasi** takrorlanmaydi
6. `PRIMARY KEY` = qaysi ikki constraint'ning birikmasi? — `UNIQUE` + `NOT NULL`
7. Jadvalda `baho = 7` bor. `CHECK (baho <= 5)` qo'shsak? — Xato: mavjud qator shartni buzadi
