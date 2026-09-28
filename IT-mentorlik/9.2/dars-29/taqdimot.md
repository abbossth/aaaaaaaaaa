# 29-dars slaydlari: PostgreSQL 🐘

## 1-slayd
🐘 **PostgreSQL** — eng kuchli ochiq kodli relatsion MBBT

## 2-slayd — Arxitektura
```
psql (terminal) ──┐
pgAdmin (GUI) ────┼──▶ PostgreSQL server :5432 ──▶ bazalar ──▶ jadvallar
Python / bot ─────┘
```

## 3-slayd — psql buyruqlari
```
psql -U postgres            -- ulanish
\l                          -- bazalar ro'yxati
CREATE DATABASE maktab;
\c maktab                   -- bazaga ulanish
\dt                         -- jadvallar
\d talabalar                -- jadval tuzilishi
\q                          -- chiqish
```

## 4-slayd — Ma'lumot turlari
| Tur | Nima uchun | Misol |
|---|---|---|
| `SERIAL` | avtomatik id | 1, 2, 3... |
| `INTEGER` / `BIGINT` | butun son / katta son (telegram_id!) | 15, 5234567890 |
| `VARCHAR(n)` | cheklangan matn | ism |
| `TEXT` | uzun matn | izoh |
| `NUMERIC(10,2)` | aniq kasr (pul!) | 12500.00 |
| `BOOLEAN` | ha/yo'q | true |
| `DATE` / `TIMESTAMP` | sana / sana-vaqt | 2026-10-01 |

## 5-slayd — CREATE TABLE
```sql
CREATE TABLE sinflar (
    id   SERIAL PRIMARY KEY,
    nom  VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE talabalar (
    id            SERIAL PRIMARY KEY,
    ism           VARCHAR(100) NOT NULL,
    tugilgan_sana DATE,
    sinf_id       INTEGER REFERENCES sinflar(id)
);
```
