# 4-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. **Juft/toq va musbat/manfiy:** son kiritilsin, masalan "Musbat juft son" deb chiqsin (4 holat + nol).
2. **Baho:** ball kiritilsin (0–100). 100 dan katta yoki manfiy bo'lsa, "Noto'g'ri ball" deb chiqsin.

## 🟡 O'rta (+10 XP)
3. **Kabisa yil:** yil kiritilsin, bitta `if` ichida `and`/`or` bilan tekshirilsin.
4. **Uchburchak:** 3 tomon kiritilsin. Uchburchak mavjudmi (har bir tomon qolgan ikkitasining yig'indisidan kichik)? Mavjud bo'lsa, turi: teng tomonli, teng yonli yoki turli tomonli.

## 🔴 Qiyin (+20 XP)
5. **Parol kuchi tekshiruvchisi:** parol kiritilsin. Qoidalar: uzunligi ≥ 8, raqam bor, katta harf bor, kichik harf bor. Natija: "Kuchsiz" (0–1 qoida bajarilgan), "O'rta" (2–3), "Kuchli" (4). Maslahat: `any(c.isdigit() for c in parol)`, `.isupper()`, `.islower()`.
6. **Kommunal tarif (bosqichli):** elektr: birinchi 200 kVt·soat — 600 so'm, 201–1000 — 1000 so'm, 1000 dan yuqorisi — 1500 so'm (har bosqich o'z narxida). Sarf kiritilsin, to'lov hisoblansin. `1200 kVt·soat` → `200×600 + 800×1000 + 200×1500 = 1 220 000`.

Yechimlar: `kod/yechimlar.py`
