-- 31-dars: constraint'lar va ALTER TABLE
-- Avval: \i ../../dars-29/kod/maktab_schema.sql  va  \i ../../dars-30/kod/maktab_data.sql

-- 1) Baho faqat 1..5 bo'lsin
ALTER TABLE baholar ADD CONSTRAINT baho_oraliq CHECK (baho BETWEEN 1 AND 5);

-- 2) O'qituvchi fani bo'sh bo'lmasin (avval bo'sh qiymatlar yo'qligini tekshiramiz)
SELECT count(*) AS bosh_fan FROM oqituvchilar WHERE fan IS NULL;
ALTER TABLE oqituvchilar ALTER COLUMN fan SET NOT NULL;

-- 3) Yangi ustun: talaba telefoni (UNIQUE) va holati (standart qiymat bilan)
ALTER TABLE talabalar ADD COLUMN telefon VARCHAR(13) UNIQUE;
ALTER TABLE talabalar ADD COLUMN faol BOOLEAN NOT NULL DEFAULT true;

-- 4) Telefon formati: +998 bilan boshlanib, 13 belgi
ALTER TABLE talabalar ADD CONSTRAINT telefon_format
    CHECK (telefon ~ '^\+998[0-9]{9}$');

-- 5) Tug'ilgan sana kelajakda bo'lishi mumkin emas
ALTER TABLE talabalar ADD CONSTRAINT sana_otmishda CHECK (tugilgan_sana < CURRENT_DATE);

-- 6) Bitta talaba bitta fandan bir kunda faqat bitta baho olsin
ALTER TABLE baholar ADD CONSTRAINT bir_kunda_bir_baho UNIQUE (talaba_id, fan, sana);

-- 7) Ustun nomini o'zgartirish va turini kengaytirish
ALTER TABLE togaraklar RENAME COLUMN nom TO nomi;
ALTER TABLE togaraklar ALTER COLUMN nomi TYPE VARCHAR(100);

-- Tekshirish
\d talabalar
