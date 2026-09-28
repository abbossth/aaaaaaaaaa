# 3-dars amaliy topshiriq

## 🟢 Oson (+5 XP): "Front yoki Back?" saralash
Har bir narsani **F** (front-end) yoki **B** (back-end) deb belgilang:
1. Instagram'dagi "yurakcha" tugmasining rangi
2. Parolning to'g'riligini tekshirish
3. Saytning qorong'u rejimi (dark mode)
4. Click'da pul o'tkazmasini hisoblash
5. YouTube'da tavsiya etilgan videolar ro'yxatini tanlash
6. Menyu ochilganda chiqadigan animatsiya
7. Telegram'da xabarlarni saqlash
8. Formadagi "Yuborish" tugmasi
9. Buyurtmani bazaga yozish
10. Sahifadagi shrift va ranglar

## 🟡 O'rta (+10 XP): `ping` tadqiqoti
`cmd` ni oching (`Win+R` → `cmd`) va quyidagilarni bajaring:
```
ping google.com
ping kun.uz
ping youtube.com
```
Jadval to'ldiring: **sayt | IP-manzil | vaqt (ms)**. Qaysi sayt eng tez javob berdi? Nega deb o'ylaysiz?

## 🔴 Qiyin (+20 XP): DNS va Network tadqiqoti
1. `nslookup kun.uz` buyrug'ini bajaring. Qanday IP chiqdi?
2. Brauzerda `F12` → **Network** tabini oching va `kun.uz` saytini yangilang (`F5`).
   - Sahifa ochilishi uchun nechta so'rov (request) ketdi?
   - Eng katta fayl qaysi?
   - Sahifa to'liq yuklanishi necha soniya oldi?

---
## Javoblar (mentor uchun)
Oson: F — 1, 3, 6, 8, 10; B — 2, 4, 5, 7, 9.
O'rta: yaqin joylashgan serverlar tezroq javob beradi (kun.uz O'zbekistonda, Google'ning esa ko'p mamlakatda serveri bor, CDN). Masofa va tarmoq yuklamasi ta'sir qiladi.
Qiyin: odatda 50–200 so'rov bo'ladi (rasmlar, reklama, skriptlar). Eng katta fayl ko'pincha rasm yoki JS bo'ladi.
