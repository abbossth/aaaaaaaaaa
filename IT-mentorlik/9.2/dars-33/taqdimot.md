# 33-dars slaydlari: JOIN 🔗

## 1-slayd
🧑‍💼 *"`talaba_id = 5` kim?!"* — ma'lumot 2 ta jadvalda. Birlashtiramiz!

## 2-slayd — INNER JOIN
```sql
SELECT t.ism, s.nom AS sinf
FROM talabalar t                 -- t = taxallus
JOIN sinflar s ON s.id = t.sinf_id;
```
Faqat **ikkala** jadvalda ham jufti borlar ⚫⚫ → ⬤

## 3-slayd — Venn diagrammalari
```
INNER:  (  [##]  )     faqat kesishma
LEFT:   (##[##]  )     chap jadval hammasi + mosi
RIGHT:  (  [##]##)     o'ng jadval hammasi + mosi
FULL:   (##[##]##)     ikkalasi ham hammasi
```

## 4-slayd — LEFT JOIN: hech kimni yo'qotmaslik
```sql
SELECT t.ism, g.nom AS togarak
FROM talabalar t
LEFT JOIN azolik a     ON a.talaba_id = t.id
LEFT JOIN togaraklar g ON g.id = a.togarak_id;
-- Madina Olimova | NULL   ← to'garaksiz
```

## 5-slayd — "Yo'qlarni" topish
```sql
SELECT t.ism FROM talabalar t
LEFT JOIN azolik a ON a.talaba_id = t.id
WHERE a.talaba_id IS NULL;      -- Sevara, Madina
```

## 6-slayd — Many-to-many: ko'prik jadval orqali
`talabalar` ⟷ **`azolik`** ⟷ `togaraklar` — 2 ta JOIN kerak

## 7-slayd — JOIN + GROUP BY
```sql
SELECT t.ism, ROUND(AVG(b.baho), 2) AS ortacha
FROM talabalar t JOIN baholar b ON b.talaba_id = t.id
GROUP BY t.id, t.ism
ORDER BY ortacha DESC;
```

## 8-slayd — ⚠️ Xatolar
- `ON` unutilsa → har bir qator har biri bilan (10 × 4 = 40 qator!) — "Dekart ko'paytmasi"
- Ikkala jadvalda `id` bor → `SELECT id` — "ambiguous" xato. Taxallus yozing: `t.id`
