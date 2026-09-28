-- 35-dars: "AI yozgan so'rovlar" — har birida xato bor. Toping va tuzating!
-- Baza: maktab (29–30-dars fayllari bilan qayta yarating)

-- Tayyorgarlik: talabasiz sinf qo'shamiz
INSERT INTO sinflar (nom) VALUES ('10.1');

-- 1) Topshiriq: "Har bir sinfdagi talabalar soni (talabasiz sinflar ham 0 bilan)"
--    AI javobi:
SELECT s.nom, COUNT(*) AS soni
FROM sinflar s
LEFT JOIN talabalar t ON t.sinf_id = s.id
GROUP BY s.nom;
-- ❓ Talabasiz sinf uchun nechta chiqadi?

-- 2) Topshiriq: "O'rtacha bahosi 4 dan yuqori talabalar ismlari"
--    AI javobi:
SELECT t.ism, AVG(b.baho)
FROM talabalar t
JOIN baholar b ON b.talaba_id = t.id
WHERE AVG(b.baho) > 4
GROUP BY t.ism;

-- 3) Topshiriq: "Telegram'i yo'q talabalar"
--    AI javobi:
SELECT ism FROM talabalar WHERE telegram_id = NULL;

-- 4) Topshiriq: "Informatika'dan 5 olganlar soni"
--    AI javobi:
SELECT COUNT(*) FROM baholar WHERE fan = 'informatika' AND baho = 5;

-- 5) Topshiriq: "Robototexnika to'garagidagi talabalar va ularning sinfi"
--    AI javobi:
SELECT t.ism, s.nom
FROM talabalar t, sinflar s, azolik a, togaraklar g
WHERE g.nom = 'Robototexnika' AND a.togarak_id = g.id AND t.id = a.talaba_id;

-- 6) Topshiriq: "Sardor Aliyevning barcha baholarini o'chir"
--    AI javobi (⚠️ ISHGA TUSHIRMANG, avval o'qing!):
-- DELETE FROM baholar WHERE talaba_id IN (SELECT id FROM talabalar WHERE ism LIKE '%Ali%');
