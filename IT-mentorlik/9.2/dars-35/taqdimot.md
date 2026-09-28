# 35-dars slaydlari: AI + SQL 🤖🗄

## 1-slayd
🤖 AI SQL'ni **juda tez** yozadi. Lekin **to'g'ri** yozadimi?

## 2-slayd — Yomon prompt ❌
> "Eng yaxshi o'quvchilarni topadigan SQL yoz"

AI jadval nomlarini **o'ylab topadi**: `students`, `grades`, `score`... 🙃

## 3-slayd — Yaxshi prompt ✅
```
Sen PostgreSQL 16 mutaxassisisan. Baza sxemasi:
<\d talabalar, \d baholar natijasi yoki CREATE TABLE lar>
Namuna ma'lumot: <har jadvaldan 3 qator>
Vazifa: o'rtacha bahosi 4.5 dan yuqori talabalar ismi va o'rtachasi, kamayish tartibida.
Talablar: faqat SELECT, izoh bilan, ROUND(…, 2).
```
**Sxema + misol + aniq vazifa + cheklov**

## 4-slayd — AI'ning tipik SQL xatolari 🐛
| Xato | Misol |
|---|---|
| `= NULL` | `WHERE telegram_id = NULL` → har doim 0 qator |
| `COUNT(*)` + LEFT JOIN | bo'sh guruh 1 bo'lib sanaladi |
| Agregat `WHERE` da | `WHERE AVG(baho) > 4` |
| Katta-kichik harf | `'informatika'` ≠ `'Informatika'` |
| Unutilgan JOIN sharti | Dekart ko'paytmasi: 3 qator → 15 qator |
| Keng `LIKE` + `DELETE` | `'%Ali%'` → Malika ham o'chadi! 😱 |

## 5-slayd — EXPLAIN ANALYZE 🔬
```sql
EXPLAIN ANALYZE SELECT * FROM katta_baholar WHERE talaba_id = 777;
-- Seq Scan ... Execution Time: 24 ms        ← indekssiz
-- Bitmap Index Scan ... Execution Time: 0.1 ms  ← indeks bilan ~200x tez!
```

## 6-slayd — Indeks = kitobning mundarijasi 📖
✅ Ko'p qidiriladigan, **kam qator** qaytaradigan ustunlar (`talaba_id`, `email`)
❌ Kichik jadvallar, 4–5 xil qiymatli ustunlar (`fan`, `jins`)
⚠️ Har bir indeks `INSERT/UPDATE` ni sekinlashtiradi va joy egallaydi

## 7-slayd — AI bilan SQL qoidalari 📜
1. Sxemani **aniq** bering
2. Natijani **qo'lda** 2–3 qatorda tekshiring
3. `UPDATE/DELETE` — faqat `BEGIN` ichida, avval `SELECT`
4. Production bazaga AI so'rovini **hech qachon** to'g'ridan-to'g'ri ishlatmang
5. Tushunmagan so'rovni ishlatmang — AI'dan tushuntirishni so'rang
