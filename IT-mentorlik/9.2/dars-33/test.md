# 33-dars tezkor test

1. Faqat ikkala jadvalda mosi borlarni qaytaradi? — `INNER JOIN`
2. Chap jadvaldagi hamma qatorlar saqlanadi? — `LEFT JOIN`
3. LEFT JOIN'da mos qator topilmasa, o'ng jadval ustunlari? — `NULL`
4. To'garaksiz talabalarni topish? — `LEFT JOIN azolik ... WHERE a.talaba_id IS NULL`
5. Many-to-many bog'lanishda nechta JOIN kerak (talaba → to'garak)? — 2 ta (ko'prik jadval orqali)
6. `column reference "id" is ambiguous` — nima qilish kerak? — Taxallus bilan yozish: `t.id`
7. `ON` sharti unutilsa nima bo'ladi? — Har bir qator har biri bilan birlashadi (Dekart ko'paytmasi)
