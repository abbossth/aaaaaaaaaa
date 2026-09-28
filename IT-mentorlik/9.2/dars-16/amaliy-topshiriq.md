# 16-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. `kod/bank.py` ni ishga tushiring. `h.balans = 999` nega ishlamayapti? `h.tarix.append("xakerlik")` qila olasizmi? Nega?
2. `Talaba` klassida `yosh` ni `@property` + setter bilan himoyalang (6..20). `ism` bo'sh bo'lmasin.

## 🟡 O'rta (+10 XP)
3. `Mahsulot` klassi: `narx` (manfiy bo'lmaydi), `chegirma` (0..90%), read-only `yakuniy_narx` (hisoblanadigan property).
4. `Termometr` klassi: ichida Selsiyda saqlaydi, lekin `fahrenheit` property'si ham bor (o'qish va yozish, avtomatik konvertatsiya). Absolyut noldan (−273.15°C) past bo'lmaydi.

## 🔴 Qiyin (+20 XP)
5. `BankHisobi` ga: 3 ta noto'g'ri PIN'dan keyin hisob bloklansin (`bloklangan` read-only property); kunlik yechish limiti 5 000 000; `pin_ozgartir(eski, yangi)` metodi (yangi PIN 4 raqamdan iborat bo'lishi shart).
6. Kontaktlar kitobi v4'da `Kontakt.tel` ni setter orqali avtomatik tozalang va tekshiring.
