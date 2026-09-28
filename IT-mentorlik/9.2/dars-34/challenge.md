# 34-dars challenge: "Server xonasidagi sirli ish" 🕵️

**Vaqt:** 45 daqiqa | **Format:** juftlikda | **Liga:** 9.2 vs 9.3 | AI va internet taqiqlanadi

## O'rnatish
```bash
createdb -U postgres sirli_ish
psql -U postgres -d sirli_ish -f kod/sirli_ish.sql
psql -U postgres -d sirli_ish
```
(pgAdmin: yangi baza `sirli_ish` → Query Tool → faylni ochish → ▶)

## Topshiriq
1. `hodisalar` jadvalidan **12-noyabr, Server xonasi** hodisasini toping.
2. Guvohlar ko'rsatmalarini o'qing.
3. Dalillarni SQL bilan tekshirib, **noutbukni olgan** odamni toping → `SELECT tekshir('...');`
4. 🤫 Bu hali oxiri emas...

## Topshirish
`tergov.sql` faylini mentorga yuboring (Telegram/GitHub). Unda har bir qadam izoh bilan:
```sql
-- 1-qadam: hodisani topdim
SELECT ...;
-- 2-qadam: ...
```

## 2-raund (tez tugatganlar uchun)
[mystery.knightlab.com](https://mystery.knightlab.com) — asl "SQL Murder Mystery" (ingliz tilida, SQLite, brauzerda). Qotilni toping, keyin "real villain"ni ham.

## Ballar
| Natija | XP |
|---|---|
| Ijrochi topildi | +30 |
| Buyurtmachi topildi | +50 |
| Knightlab qotili | +30 |
| Knightlab mastermind | +30 |
| Birinchi to'liq ochgan juftlik | +20 |
