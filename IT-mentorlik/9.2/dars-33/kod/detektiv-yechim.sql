-- 33-dars "JOIN detektiv" yechimi (mentor uchun)
SELECT DISTINCT t.ism
FROM talabalar t
JOIN azolik a1     ON a1.talaba_id = t.id
JOIN togaraklar g1 ON g1.id = a1.togarak_id AND g1.nom = 'Robototexnika'
JOIN azolik a2     ON a2.talaba_id = t.id
JOIN togaraklar g2 ON g2.id = a2.togarak_id AND g2.nom = 'Futbol'
JOIN baholar b     ON b.talaba_id = t.id AND b.fan = 'Informatika' AND b.baho = 5
JOIN sinflar s     ON s.id = t.sinf_id
JOIN oqituvchilar o ON o.id = s.rahbar_id
WHERE o.fan <> 'Informatika';
-- Javob: Temur Saidov
