-- 33-dars: JOIN — jadvallarni birlashtirish

-- 1. INNER JOIN: talaba + sinf nomi
SELECT t.ism, s.nom AS sinf
FROM talabalar t
JOIN sinflar s ON s.id = t.sinf_id
ORDER BY s.nom, t.ism;

-- 2. 3 ta jadval: talaba — sinf — sinf rahbari
SELECT t.ism AS talaba, s.nom AS sinf, o.ism AS rahbar
FROM talabalar t
JOIN sinflar s      ON s.id = t.sinf_id
JOIN oqituvchilar o ON o.id = s.rahbar_id
ORDER BY sinf, talaba;

-- 3. JOIN + GROUP BY: talaba ismi bilan o'rtacha baho (32-dars endi ism bilan!)
SELECT t.ism, COUNT(b.id) AS baholar, ROUND(AVG(b.baho), 2) AS ortacha
FROM talabalar t
JOIN baholar b ON b.talaba_id = t.id
GROUP BY t.id, t.ism
ORDER BY ortacha DESC, t.ism;

-- 4. Sinf bo'yicha o'rtacha baho
SELECT s.nom AS sinf, ROUND(AVG(b.baho), 2) AS ortacha
FROM baholar b
JOIN talabalar t ON t.id = b.talaba_id
JOIN sinflar s   ON s.id = t.sinf_id
GROUP BY s.nom
ORDER BY ortacha DESC;

-- 5. LEFT JOIN: HAMMA talabalar va ularning to'garaklari (to'garaksizlar ham chiqadi)
SELECT t.ism, g.nom AS togarak
FROM talabalar t
LEFT JOIN azolik a    ON a.talaba_id = t.id
LEFT JOIN togaraklar g ON g.id = a.togarak_id
ORDER BY t.id;

-- 6. LEFT JOIN + IS NULL: birorta ham to'garakka yozilmaganlar
SELECT t.ism
FROM talabalar t
LEFT JOIN azolik a ON a.talaba_id = t.id
WHERE a.talaba_id IS NULL;

-- 7. RIGHT JOIN (avval a'zosiz to'garak qo'shamiz)
INSERT INTO togaraklar (nom) VALUES ('Musiqa');

-- RIGHT JOIN: har bir to'garak va a'zolar soni (a'zosiz to'garak ham chiqadi)
SELECT g.nom, COUNT(a.talaba_id) AS azolar
FROM azolik a
RIGHT JOIN togaraklar g ON g.id = a.togarak_id
GROUP BY g.id, g.nom
ORDER BY azolar DESC, g.nom;

-- 8. Many-to-many: "Robototexnika" to'garagi a'zolari va sinfi
SELECT t.ism, s.nom AS sinf
FROM togaraklar g
JOIN azolik a    ON a.togarak_id = g.id
JOIN talabalar t ON t.id = a.talaba_id
JOIN sinflar s   ON s.id = t.sinf_id
WHERE g.nom = 'Robototexnika'
ORDER BY t.ism;

-- 9. Self-join g'oyasi: bir sinfdagi talabalar juftliklari
SELECT a.ism AS birinchi, b.ism AS ikkinchi, a.sinf_id
FROM talabalar a
JOIN talabalar b ON a.sinf_id = b.sinf_id AND a.id < b.id
ORDER BY a.sinf_id, a.ism;
