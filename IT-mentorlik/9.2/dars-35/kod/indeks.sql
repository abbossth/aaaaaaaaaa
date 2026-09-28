-- 35-dars: AI "optimallashtir" dedi — tekshiramiz! EXPLAIN ANALYZE va indeks
-- Alohida jadval: 1 000 000 ta "baho" (generate_series bilan soniyalarda yaratiladi)

DROP TABLE IF EXISTS katta_baholar;
CREATE TABLE katta_baholar AS
SELECT g AS id,
       (random() * 99999)::int + 1 AS talaba_id,
       (ARRAY['Informatika','Matematika','Fizika','Ingliz tili','Tarix'])[1 + (random() * 4)::int] AS fan,
       1 + (random() * 4)::int AS baho
FROM generate_series(1, 1000000) AS g;
ANALYZE katta_baholar;

-- 1) Indeks YO'Q: Seq Scan (butun jadvalni o'qiydi)
EXPLAIN ANALYZE SELECT * FROM katta_baholar WHERE talaba_id = 777;

-- 2) Indeks yaratamiz
CREATE INDEX idx_katta_baholar_talaba ON katta_baholar (talaba_id);

-- 3) Endi: Index/Bitmap Scan — "Execution Time" ni solishtiring!
EXPLAIN ANALYZE SELECT * FROM katta_baholar WHERE talaba_id = 777;

-- 4) Indeks har doim ham yordam bermaydi: jadvalning ~25% qaytadi — vaqtni 1-so'rov bilan solishtiring.
--    Ko'pincha indeks bilan ham tezlashmaydi (hatto sekinroq!). Indeks — "kam qator" qidiruv uchun.
CREATE INDEX idx_katta_baholar_fan ON katta_baholar (fan);
EXPLAIN ANALYZE SELECT * FROM katta_baholar WHERE fan = 'Fizika';

-- Tozalash
-- DROP TABLE katta_baholar;
