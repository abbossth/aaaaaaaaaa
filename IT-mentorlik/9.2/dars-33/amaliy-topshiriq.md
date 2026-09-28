# 33-dars amaliy topshiriq

Bazani yangilang (29, 30-dars fayllari). Har bir so'rovni `join-mashq.sql` ga yozing.

## 🟢 Oson (+5 XP)
1. Har bir bahoni talaba **ismi** bilan chiqaring: `ism | fan | baho | sana`.
2. Har bir sinf va uning rahbari: `sinf | rahbar | rahbar fani`.

## 🟡 O'rta (+10 XP)
3. Har bir sinfda nechta talaba bor — sinf **nomi** bilan (`LEFT JOIN`, talabasiz sinf ham 0 bilan chiqsin: avval `INSERT INTO sinflar (nom) VALUES ('10.1')`).
4. Har bir to'garak a'zolarining o'rtacha bahosi.
5. Hech qanday baho olmagan talabalar (ularni avval qo'shing).

## 🔴 Qiyin (+20 XP)
6. Har bir sinfning eng yaxshi talabasi (o'rtacha baho bo'yicha). Maslahat: `DISTINCT ON (s.nom)` yoki subquery.
7. "Dilshod Karimov" sinf rahbari bo'lgan sinf talabalarining Informatika baholari.
8. Kutubxona bazangizda (31-dars): hali qaytarilmagan kitoblar — o'quvchi ismi, kitob nomi, necha kun o'tgani (`CURRENT_DATE - olingan_sana`).
