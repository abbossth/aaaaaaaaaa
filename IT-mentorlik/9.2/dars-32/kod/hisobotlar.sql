-- 32-dars: filtrlash, agregat funksiyalar, GROUP BY / HAVING
-- Bazani yangilang: \i ../../dars-29/kod/maktab_schema.sql ; \i ../../dars-30/kod/maktab_data.sql

-- 1. Ismi "M" bilan boshlanuvchilar (LIKE / ILIKE)
SELECT ism FROM talabalar WHERE ism LIKE 'M%';

-- 2. Ismida "ov" bor (katta-kichik harf farqsiz)
SELECT ism FROM talabalar WHERE ism ILIKE '%ov%';

-- 3. IN: 9.2 va 9.3 sinflari (sinf_id 1 va 2)
SELECT ism, sinf_id FROM talabalar WHERE sinf_id IN (1, 2) ORDER BY sinf_id, ism;

-- 4. BETWEEN: 2011-yilda tug'ilganlar
SELECT ism, tugilgan_sana FROM talabalar
WHERE tugilgan_sana BETWEEN '2011-01-01' AND '2011-12-31'
ORDER BY tugilgan_sana;

-- 5. NULL bilan ishlash: Telegram'i yo'qlar (= NULL emas, IS NULL!)
SELECT ism FROM talabalar WHERE telegram_id IS NULL;

-- 6. Agregatlar: jami baholar, o'rtacha, eng past, eng yuqori
SELECT COUNT(*) AS jami, ROUND(AVG(baho), 2) AS ortacha, MIN(baho), MAX(baho), SUM(baho)
FROM baholar;

-- 7. GROUP BY: har bir fan bo'yicha o'rtacha baho
SELECT fan, COUNT(*) AS soni, ROUND(AVG(baho), 2) AS ortacha
FROM baholar
GROUP BY fan
ORDER BY ortacha DESC;

-- 8. Har bir sinfda nechta talaba
SELECT sinf_id, COUNT(*) AS talabalar_soni
FROM talabalar
GROUP BY sinf_id
ORDER BY sinf_id;

-- 9. HAVING: o'rtacha bahosi 4.5 dan yuqori talabalar (talaba_id bo'yicha)
SELECT talaba_id, ROUND(AVG(baho), 2) AS ortacha
FROM baholar
GROUP BY talaba_id
HAVING AVG(baho) > 4.5
ORDER BY ortacha DESC, talaba_id;

-- 10. WHERE + GROUP BY + HAVING birga: Informatika'dan tashqari fanlarda kamida 2 ta bahosi borlar
SELECT talaba_id, COUNT(*) AS baholar_soni
FROM baholar
WHERE fan <> 'Informatika'
GROUP BY talaba_id
HAVING COUNT(*) >= 2
ORDER BY talaba_id;

-- 11. Tug'ilgan yil bo'yicha guruhlash
SELECT EXTRACT(YEAR FROM tugilgan_sana) AS yil, COUNT(*)
FROM talabalar
GROUP BY yil
ORDER BY yil;

-- 12. CASE: baholarni so'z bilan
SELECT baho,
       CASE WHEN baho = 5 THEN 'a''lo'
            WHEN baho = 4 THEN 'yaxshi'
            WHEN baho = 3 THEN 'qoniqarli'
            ELSE 'qoniqarsiz' END AS daraja,
       COUNT(*)
FROM baholar
GROUP BY baho
ORDER BY baho DESC;
