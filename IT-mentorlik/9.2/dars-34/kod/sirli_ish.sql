-- 34-dars: "Server xonasidagi sirli ish" 🕵️ — SQL Murder Mystery (o'zbekcha versiya)
-- O'rnatish:  createdb sirli_ish   →   psql -d sirli_ish -f sirli_ish.sql
-- Tekshirish: SELECT tekshir('Ism Familiya');

DROP TABLE IF EXISTS hodisalar, korsatmalar, shaxslar, kirish_kartalari, togarak_azolari, oshxona_tolovlar CASCADE;

CREATE TABLE shaxslar (
    id        SERIAL PRIMARY KEY,
    ism       VARCHAR(60) NOT NULL,
    sinf      VARCHAR(10),          -- xodimlar uchun NULL
    lavozim   VARCHAR(30) DEFAULT 'o''quvchi',
    soch      VARCHAR(20),
    boy_sm    SMALLINT
);

CREATE TABLE hodisalar (
    id     SERIAL PRIMARY KEY,
    sana   DATE NOT NULL,
    joy    VARCHAR(40) NOT NULL,
    tavsif TEXT NOT NULL
);

CREATE TABLE korsatmalar (
    id        SERIAL PRIMARY KEY,
    hodisa_id INTEGER REFERENCES hodisalar(id),
    shaxs_id  INTEGER REFERENCES shaxslar(id),
    matn      TEXT NOT NULL
);

CREATE TABLE kirish_kartalari (
    id       SERIAL PRIMARY KEY,
    shaxs_id INTEGER REFERENCES shaxslar(id),
    xona     VARCHAR(40) NOT NULL,
    vaqt     TIMESTAMP NOT NULL,
    harakat  VARCHAR(10) CHECK (harakat IN ('kirdi', 'chiqdi'))
);

CREATE TABLE togarak_azolari (
    shaxs_id INTEGER REFERENCES shaxslar(id),
    togarak  VARCHAR(30) NOT NULL
);

CREATE TABLE oshxona_tolovlar (
    id       SERIAL PRIMARY KEY,
    shaxs_id INTEGER REFERENCES shaxslar(id),
    vaqt     TIMESTAMP NOT NULL,
    mahsulot VARCHAR(40) NOT NULL,
    summa    INTEGER NOT NULL
);

INSERT INTO shaxslar (ism, sinf, lavozim, soch, boy_sm) VALUES
 ('Anvar Qo''chqorov', NULL, 'qorovul', 'oq', 172),          -- 1
 ('Laylo Rashidova', '9.3', 'o''quvchi', 'qora', 158),         -- 2
 ('Bekzod Tursunov', '10.1', 'o''quvchi', 'qora', 181),        -- 3
 ('Doniyor Saidov', '9.2', 'o''quvchi', 'qora', 178),          -- 4
 ('Farrux Aliyev', '10.2', 'o''quvchi', 'qora', 176),          -- 5
 ('Javohir Karimov', '9.3', 'o''quvchi', 'malla', 183),        -- 6
 ('Sherzod Nurmatov', '11.2', 'o''quvchi', 'qora', 168),       -- 7
 ('Otabek Yusupov', '10.1', 'o''quvchi', 'qora', 185),         -- 8
 ('Ulug''bek Hasanov', '9.2', 'o''quvchi', 'qora', 180),       -- 9
 ('Kamola Ergasheva', '11.1', 'o''quvchi', 'qora', 165),       -- 10
 ('Nilufar Tosheva', '11.1', 'o''quvchi', 'jigarrang', 160),   -- 11
 ('Sardor Ismoilov', '11.2', 'o''quvchi', 'qora', 172),        -- 12
 ('Madina Olimova', '11.1', 'o''quvchi', 'qora', 163),         -- 13
 ('Aziz Rahimov', '8.2', 'o''quvchi', 'qora', 150),            -- 14
 ('Zarina Qodirova', '10.2', 'o''quvchi', 'jigarrang', 162),   -- 15
 ('Dilshod Karimov', NULL, 'IT o''qituvchi', 'qora', 177),     -- 16
 ('Gulnora Sobirova', NULL, 'oshpaz', 'jigarrang', 160),       -- 17
 ('Rustam Qodirov', NULL, 'direktor', 'oq', 174);              -- 18

INSERT INTO hodisalar (sana, joy, tavsif) VALUES
 ('2026-11-10', 'Sport zal', 'Futbol to''pi yirtilgan holda topildi. Aybdor topilmadi.'),
 ('2026-11-11', 'Oshxona', 'Kassada 5 000 so''m kam chiqdi. Keyin topildi — hisoblashda xato.'),
 ('2026-11-12', 'Kutubxona', 'Kitob javoni yiqilgan. Hech kim jabrlanmagan.'),
 ('2026-11-12', 'Server xonasi', 'Soat 14:00–14:30 oralig''ida IT o''qituvchisining noutbuki yo''qoldi. Guvohlar: qorovul va 9.3 sinf o''quvchisi Laylo. Ularning ko''rsatmalari korsatmalar jadvalida.'),
 ('2026-11-13', 'Server xonasi', 'Konditsioner buzildi. Texnik chaqirildi.');

INSERT INTO korsatmalar (hodisa_id, shaxs_id, matn) VALUES
 (1, 1, 'Men sport zalda hech kimni ko''rmadim.'),
 (4, 1, 'Soat 14:10 atrofida server xonasi tomondan bo''yi baland (175 sm dan ortiq), qora sochli bola yugurib o''tdi. Sumkasida "Robototexnika" to''garagi belgisi bor edi.'),
 (4, 2, 'O''sha kuni 13:00 dan 14:00 gacha oshxonada edim. Bir bola energetik ichimlik sotib oldi va juda shoshib server xonasi tomon ketdi. Yuzini ko''rmadim.'),
 (NULL, 4, 'Ha... noutbukni men oldim. Lekin bu mening g''oyam emas edi! Menga 11.1 sinfdagi bir qiz buyurdi. U "Dizayn" to''garagiga qatnashadi va noyabr oyida oshxonada kamida 3 marta pitsa olgan. Ismini bilmayman, faqat shuni eslayman.'),
 (5, 16, 'Konditsioner eski edi, buzilishi kutilgan edi.');

INSERT INTO kirish_kartalari (shaxs_id, xona, vaqt, harakat) VALUES
 (16, 'Server xonasi', '2026-11-12 13:40', 'chiqdi'),
 (5,  'Server xonasi', '2026-11-12 13:30', 'kirdi'),
 (5,  'Server xonasi', '2026-11-12 13:45', 'chiqdi'),
 (8,  'Server xonasi', '2026-11-12 14:02', 'kirdi'),
 (8,  'Server xonasi', '2026-11-12 14:04', 'chiqdi'),
 (3,  'Server xonasi', '2026-11-12 14:05', 'kirdi'),
 (3,  'Server xonasi', '2026-11-12 14:07', 'chiqdi'),
 (4,  'Server xonasi', '2026-11-12 14:08', 'kirdi'),
 (4,  'Server xonasi', '2026-11-12 14:12', 'chiqdi'),
 (6,  'Server xonasi', '2026-11-12 14:15', 'kirdi'),
 (6,  'Server xonasi', '2026-11-12 14:16', 'chiqdi'),
 (9,  'Server xonasi', '2026-11-12 14:18', 'kirdi'),
 (9,  'Server xonasi', '2026-11-12 14:21', 'chiqdi'),
 (7,  'Server xonasi', '2026-11-12 14:20', 'kirdi'),
 (7,  'Server xonasi', '2026-11-12 14:24', 'chiqdi'),
 (16, 'Server xonasi', '2026-11-12 14:35', 'kirdi'),
 (4,  'Server xonasi', '2026-11-11 14:10', 'kirdi'),
 (12, 'Server xonasi', '2026-11-11 15:00', 'kirdi'),
 (3,  'Kutubxona',     '2026-11-12 14:40', 'kirdi'),
 (2,  'Oshxona',       '2026-11-12 13:00', 'kirdi'),
 (10, 'Kompyuter xonasi', '2026-11-12 14:10', 'kirdi');

INSERT INTO togarak_azolari (shaxs_id, togarak) VALUES
 (3, 'Robototexnika'), (4, 'Robototexnika'), (5, 'Robototexnika'), (6, 'Robototexnika'),
 (7, 'Robototexnika'), (9, 'Robototexnika'), (13, 'Robototexnika'),
 (8, 'Futbol'), (3, 'Futbol'), (14, 'Futbol'),
 (10, 'Dizayn'), (11, 'Dizayn'), (12, 'Dizayn'), (15, 'Dizayn'),
 (2, 'Shaxmat'), (13, 'Shaxmat');

INSERT INTO oshxona_tolovlar (shaxs_id, vaqt, mahsulot, summa) VALUES
 (4,  '2026-11-12 13:52', 'Energetik', 12000),
 (5,  '2026-11-12 13:20', 'Energetik', 12000),
 (6,  '2026-11-12 13:10', 'Energetik', 12000),
 (7,  '2026-11-12 13:35', 'Energetik', 12000),
 (8,  '2026-11-12 13:05', 'Energetik', 12000),
 (9,  '2026-11-11 13:40', 'Energetik', 12000),
 (3,  '2026-11-12 13:30', 'Choy', 3000),
 (9,  '2026-11-12 13:25', 'Somsa', 6000),
 (2,  '2026-11-12 13:15', 'Somsa', 6000),
 (10, '2026-11-03 12:30', 'Pitsa', 18000),
 (10, '2026-11-09 12:40', 'Pitsa', 18000),
 (10, '2026-11-12 12:35', 'Pitsa', 18000),
 (10, '2026-10-28 12:30', 'Pitsa', 18000),
 (11, '2026-11-05 12:30', 'Pitsa', 18000),
 (11, '2026-11-10 12:30', 'Pitsa', 18000),
 (11, '2026-11-11 12:30', 'Choy', 3000),
 (12, '2026-11-02 12:30', 'Pitsa', 18000),
 (12, '2026-11-06 12:30', 'Pitsa', 18000),
 (12, '2026-11-12 12:30', 'Pitsa', 18000),
 (13, '2026-11-04 12:30', 'Pitsa', 18000),
 (13, '2026-11-08 12:30', 'Pitsa', 18000),
 (13, '2026-11-10 12:30', 'Pitsa', 18000),
 (13, '2026-11-12 12:30', 'Pitsa', 18000),
 (15, '2026-11-07 12:30', 'Pitsa', 18000),
 (14, '2026-11-12 13:00', 'Sharbat', 7000);

-- Javobni tekshirish funksiyasi (javoblar md5 xesh ko'rinishida — "ko'chirib" bo'lmaydi 😉)
CREATE OR REPLACE FUNCTION tekshir(gumondor TEXT) RETURNS TEXT AS $$
BEGIN
    IF md5(lower(trim(gumondor))) = 'a7a766c1035ebddc3e1e7d49a0658c84' THEN
        RETURN '🎉 To''g''ri! Noutbukni aynan u olgan. Lekin... uning so''roq paytidagi ko''rsatmasini o''qing (korsatmalar jadvalida shaxs_id bo''yicha). Haqiqiy buyurtmachini topa olasizmi? 🤔';
    ELSIF md5(lower(trim(gumondor))) = '4e817dc95826067f3ca02d0a5eaebdec' THEN
        RETURN '🏆 AJOYIB! Siz butun ishni ochdingiz — buyurtmachi topildi! Mentorga ayting: +100 XP';
    ELSE
        RETURN '❌ Yo''q, bu odam emas. Dalillarni qayta tekshiring.';
    END IF;
END;
$$ LANGUAGE plpgsql;
