-- 32-dars SQL-bingo yechimlari (mentor uchun)
SELECT ROUND(AVG(baho), 2) FROM baholar;                                         -- 4.25
SELECT COUNT(*) FROM talabalar WHERE telegram_id IS NULL;                        -- 3
SELECT fan FROM baholar GROUP BY fan ORDER BY AVG(baho) LIMIT 1;                 -- Matematika
SELECT EXTRACT(YEAR FROM tugilgan_sana) FROM talabalar
GROUP BY 1 ORDER BY COUNT(*) DESC LIMIT 1;                                       -- 2011
SELECT COUNT(*) FROM baholar WHERE baho = 5;                                     -- 10
SELECT COUNT(*) FROM (SELECT talaba_id FROM baholar GROUP BY talaba_id
                      HAVING AVG(baho) > 4.5) t;                                -- 4
SELECT ism FROM talabalar WHERE id = (SELECT talaba_id FROM baholar WHERE baho = 2); -- Sardor Aliyev
SELECT SUM(baho) FROM baholar;                                                   -- 85
SELECT COUNT(DISTINCT talaba_id) FROM baholar WHERE fan = 'Fizika';              -- 3
