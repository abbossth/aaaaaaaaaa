# 33-dars mentor eslatmasi

- `kod/server/src/app.js` (pg bilan) supertest orqali haqiqiy PostgreSQL'da tekshirilgan: health → `db: ok`, POST → 201, qisqa title → 400, GET → ro'yxat.
- Eski `docker-compose` (defis bilan, v1) emas, `docker compose` (v2) ishlatamiz. Compose faylida `version:` qatori endi kerak emas.
- Jamoalar `db.json` → PostgreSQL o'tishida qiynalsa: `pg` bilan faqat 3 ta so'rov kerak (CREATE TABLE IF NOT EXISTS, SELECT, INSERT ... RETURNING). SQL'ni 9.2 guruhi materiallaridan eslatish mumkin: `../../9.2/dars-30/`.
- Windows'da bind mount + `node --watch` sekin ishlashi mumkin (WSL2 fayl tizimi). Loyihani WSL ichida saqlash tavsiya etiladi.
- `docker compose down -v` ni ogohlantirib ko'rsating — real loyihalarda shu buyruq bilan baza yo'qotilgan holatlar ko'p.
