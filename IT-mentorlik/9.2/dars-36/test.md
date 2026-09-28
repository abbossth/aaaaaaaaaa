# 36-dars tezkor test

1. asyncpg'da bitta qiymat qaytaradigan metod? — `fetchval`
2. Parametrli so'rovda o'rin belgisi? — `$1, $2, ...`
3. f-string bilan SQL yozish nega xavfli? — SQL injection: foydalanuvchi matni buyruq sifatida bajarilishi mumkin
4. `ON CONFLICT (telegram_id) DO UPDATE` nima qiladi? — Yozuv bor bo'lsa yangilaydi, yo'q bo'lsa qo'shadi (UPSERT)
5. Tranzaksiya nima uchun? — Bir nechta amal hammasi birga bajarilishi yoki birga bekor qilinishi uchun
6. `RETURNING` nima beradi? — O'zgartirilgan qator(lar) qiymatini shu so'rovning o'zida qaytaradi
7. Nega har bir handlerda yangi ulanish emas, pool? — Ulanish ochish qimmat; pool tayyor ulanishlarni qayta ishlatadi
