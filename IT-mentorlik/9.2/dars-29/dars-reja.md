# 29-dars. PostgreSQL: o'rnatish, psql, pgAdmin, CREATE DATABASE/TABLE, ma'lumot turlari

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 3-bob, "PostgreSQL: o'rnatish, MB va jadvallar yaratish, ma'lumotlarning asosiy toifalari"

## Maqsad
- PostgreSQL arxitekturasini sodda tushunadi: server (5432-port) va mijozlar (psql, pgAdmin, Python).
- `psql` buyruqlar qatori va **pgAdmin** grafik interfeysi bilan ishlaydi.
- Ma'lumotlar bazasi yaratadi, ulanadi: `CREATE DATABASE`, `\c`, `\l`, `\dt`, `\d jadval`.
- Asosiy ma'lumot turlarini biladi: `SERIAL/INTEGER/BIGINT`, `VARCHAR(n)/TEXT`, `NUMERIC(p,s)`, `BOOLEAN`, `DATE/TIMESTAMP`.
- 28-darsdagi ER-diagramma asosida jadvallar yaratadi (`CREATE TABLE`), PK va FK bilan.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Instagram, Spotify, Apple, Reddit — PostgreSQL ishlatadi. Bugun o'z kompyuteringizda o'sha MBBT'ni ishga tushirasiz."* |
| 5–20 | **O'rnatish tekshiruvi** | Kim o'rnatgan, kimda muammo. Muqobillar (Docker / neon.tech) |
| 20–35 | **Yangi mavzu** | Arxitektura. psql buyruqlari. Turlar jadvali. `CREATE TABLE` sintaksisi |
| 35–60 | **Amaliyot** | `amaliy-topshiriq.md`: "maktab" bazasi |
| 60–72 | **Challenge** | `challenge.md`: "Tur tanlash" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- PostgreSQL ishlaydi +10 · Amaliyot +5/+10/+20 · Challenge +20/+10/+5
