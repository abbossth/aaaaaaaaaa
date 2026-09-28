-- 34-dars: "Server xonasidagi sirli ish" — to'liq yechim (FAQAT MENTOR UCHUN!)

-- 1-qadam: hodisani topish
SELECT * FROM hodisalar WHERE sana = '2026-11-12' AND joy = 'Server xonasi';

-- 2-qadam: guvohlar ko'rsatmalari
SELECT s.ism, k.matn FROM korsatmalar k JOIN shaxslar s ON s.id = k.shaxs_id WHERE k.hodisa_id = 4;

-- 3-qadam: barcha dalillarni birlashtirish
SELECT DISTINCT s.ism, s.sinf, s.boy_sm, s.soch
FROM shaxslar s
JOIN kirish_kartalari kk ON kk.shaxs_id = s.id
JOIN togarak_azolari t   ON t.shaxs_id = s.id
JOIN oshxona_tolovlar o  ON o.shaxs_id = s.id
WHERE kk.xona = 'Server xonasi'
  AND kk.harakat = 'kirdi'
  AND kk.vaqt BETWEEN '2026-11-12 14:00' AND '2026-11-12 14:30'
  AND s.boy_sm > 175
  AND s.soch = 'qora'
  AND t.togarak = 'Robototexnika'
  AND o.mahsulot = 'Energetik'
  AND o.vaqt::date = '2026-11-12';
-- → Doniyor Saidov

SELECT tekshir('Doniyor Saidov');

-- 4-qadam (bonus): aybdorning ko'rsatmasi
SELECT matn FROM korsatmalar WHERE shaxs_id = (SELECT id FROM shaxslar WHERE ism = 'Doniyor Saidov');

-- 5-qadam: buyurtmachi — 11.1, Dizayn, noyabrda >= 3 ta pitsa
SELECT s.ism, COUNT(*) AS pitsalar
FROM shaxslar s
JOIN togarak_azolari t  ON t.shaxs_id = s.id AND t.togarak = 'Dizayn'
JOIN oshxona_tolovlar o ON o.shaxs_id = s.id
WHERE s.sinf = '11.1'
  AND o.mahsulot = 'Pitsa'
  AND o.vaqt >= '2026-11-01' AND o.vaqt < '2026-12-01'
GROUP BY s.id, s.ism
HAVING COUNT(*) >= 3;
-- → Kamola Ergasheva

SELECT tekshir('Kamola Ergasheva');
