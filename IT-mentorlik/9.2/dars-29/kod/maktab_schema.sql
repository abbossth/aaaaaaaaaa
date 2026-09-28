-- "Maktab" bazasi sxemasi (28-darsdagi ER-diagramma asosida)
-- psql:   \i maktab_schema.sql      pgAdmin: Query Tool → ochish → ▶

DROP TABLE IF EXISTS baholar, azolik, togaraklar, talabalar, sinflar, oqituvchilar CASCADE;

CREATE TABLE oqituvchilar (
    id   SERIAL PRIMARY KEY,
    ism  VARCHAR(100) NOT NULL,
    fan  VARCHAR(50)
);

CREATE TABLE sinflar (
    id        SERIAL PRIMARY KEY,
    nom       VARCHAR(10) NOT NULL UNIQUE,
    rahbar_id INTEGER REFERENCES oqituvchilar(id)
);

CREATE TABLE talabalar (
    id            SERIAL PRIMARY KEY,
    ism           VARCHAR(100) NOT NULL,
    tugilgan_sana DATE,
    sinf_id       INTEGER REFERENCES sinflar(id),
    telegram_id   BIGINT UNIQUE,
    yaratilgan    TIMESTAMP DEFAULT now()
);

CREATE TABLE togaraklar (
    id   SERIAL PRIMARY KEY,
    nom  VARCHAR(50) NOT NULL
);

CREATE TABLE azolik (
    talaba_id  INTEGER REFERENCES talabalar(id) ON DELETE CASCADE,
    togarak_id INTEGER REFERENCES togaraklar(id) ON DELETE CASCADE,
    sana       DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (talaba_id, togarak_id)
);

CREATE TABLE baholar (
    id        SERIAL PRIMARY KEY,
    talaba_id INTEGER NOT NULL REFERENCES talabalar(id) ON DELETE CASCADE,
    fan       VARCHAR(50) NOT NULL,
    baho      SMALLINT NOT NULL,
    sana      DATE DEFAULT CURRENT_DATE
);
