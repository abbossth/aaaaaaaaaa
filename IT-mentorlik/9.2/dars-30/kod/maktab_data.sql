-- "Maktab" bazasi uchun namuna ma'lumotlar (avval maktab_schema.sql ni ishga tushiring)

INSERT INTO oqituvchilar (ism, fan) VALUES
    ('Dilshod Karimov', 'Informatika'),
    ('Nodira Aliyeva', 'Matematika'),
    ('Rustam Qodirov', 'Fizika'),
    ('Gulnora Sobirova', 'Ingliz tili');

INSERT INTO sinflar (nom, rahbar_id) VALUES
    ('9.2', 1), ('9.3', 2), ('8.2', 3), ('11.1', 4);

INSERT INTO talabalar (ism, tugilgan_sana, sinf_id, telegram_id) VALUES
    ('Aziz Karimov',     '2011-03-14', 1, 5100000001),
    ('Malika Yusupova',  '2011-07-22', 1, 5100000002),
    ('Bobur Rahimov',    '2011-01-05', 1, NULL),
    ('Dilnoza Tosheva',  '2011-11-30', 2, 5100000004),
    ('Sardor Aliyev',    '2010-12-12', 2, 5100000005),
    ('Nigora Hasanova',  '2011-05-18', 2, NULL),
    ('Jasur Ergashev',   '2012-02-02', 3, 5100000007),
    ('Madina Olimova',   '2012-09-09', 3, 5100000008),
    ('Temur Saidov',     '2009-04-04', 4, 5100000009),
    ('Sevara Nazarova',  '2009-08-19', 4, NULL);

INSERT INTO togaraklar (nom) VALUES ('Robototexnika'), ('Shaxmat'), ('Futbol'), ('Dizayn');

INSERT INTO azolik (talaba_id, togarak_id) VALUES
    (1, 1), (1, 2), (2, 4), (3, 3), (4, 1), (5, 3), (6, 4), (7, 2), (9, 1), (9, 3);

INSERT INTO baholar (talaba_id, fan, baho, sana) VALUES
    (1, 'Informatika', 5, '2026-10-01'), (1, 'Matematika', 4, '2026-10-02'), (1, 'Fizika', 5, '2026-10-03'),
    (2, 'Informatika', 5, '2026-10-01'), (2, 'Matematika', 5, '2026-10-02'), (2, 'Fizika', 5, '2026-10-03'),
    (3, 'Informatika', 3, '2026-10-01'), (3, 'Matematika', 4, '2026-10-02'), (3, 'Fizika', 3, '2026-10-03'),
    (4, 'Informatika', 4, '2026-10-01'), (4, 'Matematika', 5, '2026-10-02'),
    (5, 'Informatika', 3, '2026-10-01'), (5, 'Matematika', 2, '2026-10-02'),
    (6, 'Informatika', 5, '2026-10-01'), (6, 'Matematika', 4, '2026-10-02'),
    (7, 'Informatika', 4, '2026-10-01'), (8, 'Informatika', 5, '2026-10-01'),
    (9, 'Informatika', 5, '2026-10-01'), (9, 'Matematika', 5, '2026-10-02'),
    (10, 'Informatika', 4, '2026-10-01');
