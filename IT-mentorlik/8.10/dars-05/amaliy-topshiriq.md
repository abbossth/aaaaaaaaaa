# 5-dars amaliy topshiriq (Flowgorithm)

## 🟢 Oson (+5 XP)
1. **Juft/toq:** son kiritilsin, "Juft" yoki "Toq" deb chiqarilsin.
2. **Musbat/manfiy:** son kiritilsin, "Musbat", "Manfiy" yoki "Nol" deb chiqarilsin (ichma-ich If).

## 🟡 O'rta (+10 XP)
3. **Baho aniqlagich:** 0–100 ball kiritilsin, baho chiqarilsin (86+ → 5, 71+ → 4, 56+ → 3, qolgani → 2).
4. **Kattasi:** ikki son kiritilsin, kattasini chiqaring. Teng bo'lsa, "Teng" deb yozilsin.

## 🔴 Qiyin (+20 XP)
5. **Kinoteatr kassasi:** yosh va kun kiritiladi.
   - 7 yoshgacha → bepul
   - 7–17 yosh → 20 000 so'm
   - 18+ → 35 000 so'm
   - Shanba yoki yakshanba bo'lsa, narxga 10 000 so'm qo'shiladi (bepul chiptadan tashqari)
6. **Kabisa yil:** yil kiritilsin. Yil 4 ga bo'linsa VA 100 ga bo'linmasa YOKI 400 ga bo'linsa, kabisa yil hisoblanadi. `2024` → kabisa, `1900` → yo'q, `2000` → kabisa.

---
## Tekshirish uchun sinov qiymatlari (mentor uchun)
- 3: 100→5, 86→5, 85→4, 71→4, 70→3, 56→3, 55→2, 0→2
- 5: (5, dushanba)→0; (12, shanba)→30 000; (30, seshanba)→35 000; (30, yakshanba)→45 000
- 6: `(yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0`
