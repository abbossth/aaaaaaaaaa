# 36-dars mentor eslatmasi

- `kod/db.py` haqiqiy PostgreSQL 16'da `sinov.py` orqali tekshirilgan (olish → "ok", qayta olish → "allaqachon", qaytarish → True, statistika). `bot.py` aiogram 3 bilan import tekshirilgan.
- `schema.sql` `db.ulan()` da har safar bajariladi (`IF NOT EXISTS` va `WHERE NOT EXISTS` tufayli xavfsiz). Real loyihalarda buning o'rniga migratsiyalar — Alembic (45-dars).
- Windows'da `DATABASE_URL` dagi parolda `@` yoki `#` bo'lsa, URL buziladi — parolni oddiyroq qiling yoki URL-encode (`%40`).
- "Hacker hujumi"da SQL injection ishlamasligi kerak (parametrli so'rovlar). Agar biror jamoada ishlasa — bu dars uchun eng yaxshi "o'rgatuvchi" hodisa, butun sinfga ko'rsating.
- Tez tugatgan jamoalarga: bot + bazani 9.3 dagi raqib jamoa bilan solishtirish (liga oldidan razminka).
