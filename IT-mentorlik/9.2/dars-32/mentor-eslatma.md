# 32-dars mentor eslatmasi

- `kod/hisobotlar.sql` natijalari tekshirilgan (toza bazada): jami 20 baho, o'rtacha 4.25; eng past o'rtacha — Matematika 4.14; o'rtachasi 4.5 dan yuqori — talaba_id 2, 8, 9 (5.00) va 1 (4.67).
- Bingo javoblari: `SELECT COUNT(*) FROM baholar WHERE fan='Fizika'` → 3; `COUNT(*) FILTER (WHERE baho=5)` → 10; eng ko'p tug'ilgan yil — 2011 (5 ta).
- Eng ko'p xato: `SELECT ism, COUNT(*) FROM talabalar GROUP BY sinf_id` → "must appear in the GROUP BY clause". Buni ataylab ko'rsating.
- `COUNT(*)` vs `COUNT(ustun)` farqini `telegram_id` misolida ko'rsating: 10 va 7.
