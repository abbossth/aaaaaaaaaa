-- 36-dars: "Kutubxona bot" bazasi
CREATE TABLE IF NOT EXISTS foydalanuvchilar (
    telegram_id BIGINT PRIMARY KEY,
    ism         VARCHAR(100) NOT NULL,
    username    VARCHAR(64),
    qoshilgan   TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS kitoblar (
    id       SERIAL PRIMARY KEY,
    nomi     VARCHAR(200) NOT NULL,
    muallif  VARCHAR(100) NOT NULL,
    soni     INTEGER NOT NULL DEFAULT 1 CHECK (soni >= 0)
);

CREATE TABLE IF NOT EXISTS ijaralar (
    id          SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL REFERENCES foydalanuvchilar(telegram_id) ON DELETE CASCADE,
    kitob_id    INTEGER NOT NULL REFERENCES kitoblar(id),
    olingan     TIMESTAMPTZ DEFAULT now(),
    qaytarilgan TIMESTAMPTZ
);

INSERT INTO kitoblar (nomi, muallif, soni)
SELECT * FROM (VALUES
    ('O''tkan kunlar', 'Abdulla Qodiriy', 3),
    ('Sariq devni minib', 'Xudoyberdi To''xtaboyev', 2),
    ('Shum bola', 'G''afur G''ulom', 2),
    ('Python Crash Course', 'Eric Matthes', 1),
    ('Clean Code', 'Robert C. Martin', 1)
) AS v(nomi, muallif, soni)
WHERE NOT EXISTS (SELECT 1 FROM kitoblar);
