# 35-dars tezkor test

1. Text-to-SQL prompt'ida eng muhim narsa? — Baza sxemasi (jadvallar va ustunlar)
2. `COUNT(*)` va `COUNT(t.id)` LEFT JOIN'da farqi? — `COUNT(*)` bo'sh (NULL) qatorni ham sanaydi
3. `EXPLAIN ANALYZE` nima ko'rsatadi? — So'rov rejasi va haqiqiy bajarilish vaqti
4. `Seq Scan` nima? — Butun jadvalni boshidan oxirigacha o'qish
5. Indeks qachon foydasiz? — Kichik jadval yoki so'rov jadvalning katta qismini qaytarsa
6. AI yozgan `DELETE` ni qanday xavfsiz sinaymiz? — `BEGIN;` → avval `SELECT` → `DELETE` → tekshirish → `COMMIT`/`ROLLBACK`
