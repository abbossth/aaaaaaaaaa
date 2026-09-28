# 29-dars mentor eslatmasi

## O'rnatish muammolari
| Muammo | Yechim |
|---|---|
| `psql` topilmadi (Windows) | PATH'ga `C:\Program Files\PostgreSQL\16\bin` qo'shish yoki "SQL Shell (psql)" dasturini ishlatish |
| Parol unutilgan | Qayta o'rnatish (yoki `pg_hba.conf` da vaqtincha `trust`, faqat mentor) |
| Konsol'da o'zbekcha harflar buzilgan | psql'da `\encoding UTF8`, Windows konsolida `chcp 65001` |
| O'rnatib bo'lmaydi | Docker: `docker run --name pg -e POSTGRES_PASSWORD=parol -p 5432:5432 -d postgres:16` yoki **neon.tech** (bepul bulut) |

- `kod/maktab_schema.sql` keyingi darslarda (30–34) ishlatiladi. 30-darsda `maktab_data.sql` (ma'lumotlar) qo'shiladi.
