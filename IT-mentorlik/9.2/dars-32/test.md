# 32-dars tezkor test

1. Ismi "A" bilan boshlanuvchilar? — `WHERE ism LIKE 'A%'`
2. NULL qiymatni tekshirish? — `IS NULL` (`= NULL` emas)
3. `BETWEEN 3 AND 5` — 3 va 5 kiradimi? — Ha, ikkalasi ham
4. Guruhlarni filtrlash uchun? — `HAVING`
5. `WHERE AVG(baho) > 4` — nega xato? — Agregat funksiyani `WHERE` da ishlatib bo'lmaydi, `HAVING` kerak
6. `COUNT(*)` va `COUNT(telegram_id)` farqi? — Ikkinchisi `NULL` qiymatlarni sanamaydi
7. `GROUP BY` qaysi bosqichdan keyin bajariladi? — `WHERE` dan keyin
