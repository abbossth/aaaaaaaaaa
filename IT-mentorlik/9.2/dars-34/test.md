# 34-dars tezkor test (dars oxirida refleksiya)

1. Noma'lum bazada qaysi jadvallar borligini qanday bilamiz? — `\dt`
2. Jadval tuzilishini ko'rish? — `\d jadval_nomi`
3. `TIMESTAMP` ustunidan faqat sanani olish? — `vaqt::date` (yoki `DATE(vaqt)`)
4. Bir odamga tegishli 3 xil dalilni bitta so'rovda tekshirish? — Bir nechta `JOIN` + `WHERE ... AND ...`
5. "Kamida 3 marta pitsa olgan" sharti? — `GROUP BY ... HAVING COUNT(*) >= 3`
6. Nega `tekshir()` da javob ochiq matn emas, md5? — Funksiya kodini ko'rsa ham javobni bilib bo'lmasligi uchun
