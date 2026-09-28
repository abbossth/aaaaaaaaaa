# 35-dars. 🤖 AI + SQL: text-to-SQL, AI so'rovlarini tekshirish va optimallashtirish

**Guruh:** 9.2 / 9.3 | **Turi:** 🤖 AI | **Davomiyligi:** 80 daqiqa

## Maqsad
- AI'ga baza sxemasini to'g'ri berib, "text-to-SQL" prompt yozadi.
- AI yozgan so'rovni **ko'r-ko'rona ishlatmaydi**: natijani qo'lda tekshiradi, tipik AI xatolarini taniydi (NULL, COUNT(*) + LEFT JOIN, WHERE/HAVING, katta-kichik harf, bog'lanmagan jadval, xavfli DELETE).
- `EXPLAIN ANALYZE` ni o'qiydi: Seq Scan vs Index Scan, Execution Time.
- Indeks qachon yordam berishini va qachon bermasligini tajribada ko'radi.
- Xavfli so'rovlarni tranzaksiyada (`BEGIN ... ROLLBACK/COMMIT`) sinaydi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Murder Mystery g'olibi e'lon qilinadi 🏆. Keyin: *"AI bu sirni 10 soniyada yechadimi?"* — jonli sinov (odatda noto'g'ri yoki yarim javob beradi) |
| 5–15 | **Yangi mavzu 1** | `taqdimot.md` 1–4: yaxshi text-to-SQL prompt tuzilishi |
| 15–38 | **"AI xatolari ovi"** | `kod/ai_xatolari.sql` — 6 ta AI so'rovi, har biri xatoli. Juftlikda topish, keyin tahlil |
| 38–55 | **Yangi mavzu 2 + jonli** | `kod/indeks.sql`: 1 000 000 qator, EXPLAIN ANALYZE, indeks |
| 55–72 | **Challenge** | `challenge.md`: "Inson vs AI" |
| 72–80 | **Yakun** | AI bilan ishlash qoidalari (7-slayd), XP |

## Baholash (XP)
- Har bir topilgan AI xatosi +4 · Amaliyot +5/+10/+20 · Challenge 🥇 +20
