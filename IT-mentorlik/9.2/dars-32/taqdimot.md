# 32-dars slaydlari: Hisobotlar 📊

## 1-slayd
🧑‍💼 Direktor: *"Qaysi fan eng qiyin? Kim a'lochi? Ertaga ertalabgacha!"*

## 2-slayd — Filtr operatorlari
| Operator | Misol |
|---|---|
| `LIKE 'M%'` | M bilan boshlanadi (`%` = istalgan belgilar, `_` = bitta belgi) |
| `ILIKE '%ov%'` | katta-kichik harf farqsiz |
| `IN (1, 2)` | ro'yxatdagi qiymatlardan biri |
| `BETWEEN a AND b` | oraliqda (chegaralar kiradi) |
| `IS NULL` | bo'sh (❌ `= NULL` ishlamaydi!) |

## 3-slayd — Agregat funksiyalar
```sql
SELECT COUNT(*), ROUND(AVG(baho), 2), MIN(baho), MAX(baho), SUM(baho)
FROM baholar;
-- 20 | 4.25 | 2 | 5 | 85
```
Ko'p qator → **bitta** natija

## 4-slayd — GROUP BY = "qutilarga ajrat, har birini sana"
```sql
SELECT fan, ROUND(AVG(baho), 2) AS ortacha
FROM baholar
GROUP BY fan
ORDER BY ortacha;
-- Matematika 4.14 ← eng qiyin fan!
```
⚠️ `SELECT` dagi har bir ustun yo `GROUP BY` da, yo agregat ichida bo'lishi shart

## 5-slayd — WHERE vs HAVING
| | WHERE | HAVING |
|---|---|---|
| Qachon? | Guruhlashdan **oldin** | Guruhlashdan **keyin** |
| Nimani filtrlaydi? | Qatorlarni | Guruhlarni |
| Agregat ishlatsa bo'ladimi? | ❌ | ✅ |

## 6-slayd — So'rov bajarilish tartibi
`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`

## 7-slayd — CASE = SQL'dagi if
```sql
CASE WHEN baho = 5 THEN 'a''lo' WHEN baho = 4 THEN 'yaxshi' ELSE 'boshqa' END
```
