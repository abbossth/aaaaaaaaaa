-- 35-dars: AI xatolarining yechimlari (mentor uchun)

-- 1) COUNT(*) bo'sh LEFT JOIN qatorini ham sanaydi → talabasiz sinf 1 bo'lib chiqadi
SELECT s.nom, COUNT(t.id) AS soni
FROM sinflar s
LEFT JOIN talabalar t ON t.sinf_id = s.id
GROUP BY s.id, s.nom
ORDER BY s.nom;

-- 2) Agregat WHERE'da emas, HAVING'da; bir xil ismli ikki talaba birlashib ketmasin — t.id bo'yicha guruhlash
SELECT t.ism, ROUND(AVG(b.baho), 2) AS ortacha
FROM talabalar t
JOIN baholar b ON b.talaba_id = t.id
GROUP BY t.id, t.ism
HAVING AVG(b.baho) > 4
ORDER BY ortacha DESC;

-- 3) NULL bilan = ishlamaydi
SELECT ism FROM talabalar WHERE telegram_id IS NULL;

-- 4) Katta-kichik harf: bazada 'Informatika' → natija 0 bo'lardi
SELECT COUNT(*) FROM baholar WHERE fan = 'Informatika' AND baho = 5;

-- 5) sinflar jadvali bog'lanmagan → har bir talaba 4 marta (har bir sinf bilan) chiqadi
SELECT t.ism, s.nom
FROM togaraklar g
JOIN azolik a    ON a.togarak_id = g.id
JOIN talabalar t ON t.id = a.talaba_id
JOIN sinflar s   ON s.id = t.sinf_id
WHERE g.nom = 'Robototexnika';

-- 6) '%Ali%' → "Aliyev" ham, "Malika" ham... (Malika Yusupova, Sardor Aliyev) — boshqa odamning baholari ham o'chadi!
--    To'g'ri yo'l: avval SELECT bilan tekshirish, aniq id bilan, tranzaksiya ichida
BEGIN;
SELECT id, ism FROM talabalar WHERE ism = 'Sardor Aliyev';
DELETE FROM baholar WHERE talaba_id = (SELECT id FROM talabalar WHERE ism = 'Sardor Aliyev');
-- natijani tekshiring, keyin COMMIT; yoki xato bo'lsa ROLLBACK;
ROLLBACK;
