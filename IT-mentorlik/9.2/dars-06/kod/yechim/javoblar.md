# Bug Hunt #1 — javoblar (faqat mentor uchun!)

| № | Xato | Turi | Tuzatish |
|---|---|---|---|
| 1 | Yopuvchi qavs yo'q | Sintaksis | `print("Salom, " + ism + "!")` |
| 2 | `input` str qaytaradi, `2026 - "2010"` | Runtime (TypeError) | `yil = int(input(...))` |
| 3 | `=` o'rniga `==` | Sintaksis | `if son % 2 == 0:` |
| 4 | Shartlar tartibi teskari: 95 ham 3 chiqadi | Mantiqiy | Kattadan kichikka: `>= 86`, `>= 71`, `>= 56` |
| 5 | `range(1, 10)` 10 ni o'z ichiga olmaydi → 45 | Mantiqiy | `range(1, 11)` |
| 6 | Amallar ustuvorligi: faqat `c` 3 ga bo'linadi | Mantiqiy | `(a + b + c) / 3` |
| 7 | Shart teskari: to'g'ri parolda "Xato" deydi | Mantiqiy | `if parol != "python2026":` |
| 8 | `n = 1` (va 0, manfiy) uchun "Tub" chiqadi | Mantiqiy | Boshida `if n < 2: tub = False`. Bonus: `range(2, int(n**0.5)+1)` va `break` |
| 9 | 2 ta xato: `natija = 0` (doim 0) va `i < n` (n kirmaydi) | Mantiqiy | `natija = 1`, `while i <= n` |
| 10 | 2 ta xato: `elif` tartibi (600 000 → 10%) va 50 000 da `chegirma` aniqlanmagan (NameError) | Mantiqiy + Runtime | Avval `>= 500000`, keyin `>= 100000`, `else: chegirma = 0` |
