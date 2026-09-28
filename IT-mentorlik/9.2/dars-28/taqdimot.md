# 28-dars slaydlari: Ma'lumotlar bazasi 🗄

## 1-slayd
**1 milliard foydalanuvchi — JSON faylda? 😱**

## 2-slayd — JSON faylning muammolari
❌ 2 kishi bir vaqtda yozsa — ma'lumot yo'qoladi
❌ 1 000 000 yozuvdan qidirish — butun faylni o'qish kerak (sekin)
❌ Noto'g'ri ma'lumot (yosh = "abc") ni hech kim to'xtatmaydi
❌ Zaxira, huquqlar, tranzaksiyalar yo'q

## 3-slayd — MB va MBBT
**Ma'lumotlar bazasi (MB)** — tartiblangan ma'lumotlar to'plami
**MBBT (DBMS)** — MB'ni boshqaruvchi dastur: PostgreSQL, MySQL, SQLite, Oracle
**SQL** — MBBT bilan "gaplashish" tili

## 4-slayd — Relatsion vs NoSQL
| Relatsion (SQL) | NoSQL |
|---|---|
| Jadvallar, qat'iy tuzilma | Hujjatlar (JSON), kalit-qiymat, graf |
| PostgreSQL, MySQL | MongoDB, Redis |
| Bank, do'kon, maktab | Kesh, chat, loglar |

## 5-slayd — Jadval
```
talabalar
┌────┬─────────┬──────┬──────────┐
│ id │ ism     │ yosh │ sinf_id  │  ← ustunlar (maydonlar)
├────┼─────────┼──────┼──────────┤
│ 1  │ Aziz    │ 15   │ 2        │  ← qator (yozuv)
│ 2  │ Malika  │ 14   │ 3        │
└────┴─────────┴──────┴──────────┘
 PK                      FK → sinflar.id
```

## 6-slayd — Bog'lanishlar
**1:1** — odam ↔ pasport
**1:N** — sinf → ko'p talabalar (FK talabalarda)
**N:M** — talabalar ↔ to'garaklar (oraliq jadval: `azolik(talaba_id, togarak_id)`)

## 7-slayd — Normalizatsiya
❌ Yomon:
| buyurtma | mijoz | mijoz_tel | mahsulotlar |
|---|---|---|---|
| 1 | Aziz | 90123 | non, sut, choy |
✅ Yaxshi: `mijozlar`, `mahsulotlar`, `buyurtmalar`, `buyurtma_qatorlari`
Qoida: **har bir fakt faqat bir joyda saqlanadi**
