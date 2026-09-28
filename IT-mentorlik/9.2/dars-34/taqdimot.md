# 34-dars slaydlari: Sirli ish 🕵️

## 1-slayd
🔦 **12-noyabr, 14:00–14:30. Server xonasi. Noutbuk yo'qoldi.**
Siz — SQL detektivsiz. Qurolingiz: `SELECT` 🔍

## 2-slayd — Qoidalar
- Faqat **SQL** bilan. Taxmin qilib ism yozish — mumkin emas, har bir xulosa so'rov bilan isbotlanadi.
- AI taqiqlanadi 🚫🤖, internetda qidirish taqiqlanadi.
- Juftlik ichida gaplashish mumkin, boshqa juftliklarga yordam — diskvalifikatsiya.
- Har bir so'rovni `tergov.sql` fayliga yozib boring (izohlar bilan) — mentor tekshiradi.

## 3-slayd — Baza xaritasi
```
shaxslar ─┬─ korsatmalar ── hodisalar
          ├─ kirish_kartalari   (kim, qaysi xonaga, qachon)
          ├─ togarak_azolari
          └─ oshxona_tolovlar   (kim, nima, qachon)
```

## 4-slayd — Birinchi qadamlar
```sql
\dt                           -- qanday jadvallar bor?
\d kirish_kartalari           -- ustunlari qanday?
SELECT * FROM hodisalar;      -- nima bo'lgan?
```

## 5-slayd — Foydali qurollar 🧰
- Vaqt oralig'i: `vaqt BETWEEN '2026-11-12 14:00' AND '2026-11-12 14:30'`
- Faqat sana: `vaqt::date = '2026-11-12'`
- Bir nechta dalil: `JOIN` + `JOIN` + `JOIN` + `WHERE ... AND ...`
- Sanash: `GROUP BY ... HAVING COUNT(*) >= 3`

## 6-slayd — Javobni tekshirish
```sql
SELECT tekshir('Ism Familiya');
```
⚠️ Ikki bosqich bor: **ijrochi** va... 🤫
