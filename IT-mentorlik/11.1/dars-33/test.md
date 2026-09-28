# 33-dars tezkor test

1. Compose'da server bazaga qaysi host nomi bilan ulanadi? — Xizmat nomi (`db`)
2. Konteyner ichida `localhost` nimani anglatadi? — Konteynerning o'zini
3. Baza ma'lumotlari uchun qaysi volume turi? — Named volume
4. `docker compose down -v` nima qiladi? — Konteynerlar, tarmoq **va volume**'larni o'chiradi
5. `depends_on: [db]` baza tayyor bo'lishini kutadimi? — Yo'q, faqat tartib; `condition: service_healthy` kerak
6. Parolni compose faylida qanday yashiramiz? — `.env` fayl va `${O'ZGARUVCHI}`
7. Nega `db` xizmatida `ports` yozilmaydi? — Baza faqat ichki tarmoqda bo'lsin, tashqaridan ochiq bo'lmasin
