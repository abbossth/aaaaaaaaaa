# 9-dars amaliy topshiriq: "Kontaktlar kitobi" v1 📒

Bu loyiha 10–11-darslarda davom ettiriladi: v2 — funksiyalar, v3 — fayl va xatolar.

## 🟢 Oson (+5 XP)
Kontaktlar dict'da saqlanadi: kalit — ism, qiymat — telefon. Menyu:
```
1. Kontakt qo'shish
2. Barcha kontaktlar
3. Qidirish (ism bo'yicha)
0. Chiqish
```

## 🟡 O'rta (+10 XP)
Qiymat ichma-ich dict bo'lsin: `{"tel": ..., "email": ..., "guruh": ...}`. Qo'shimcha menyu:
```
4. Kontaktni tahrirlash
5. Kontaktni o'chirish
6. Guruh bo'yicha filtrlash (do'st, oila, sinfdosh)
```
Ism takrorlansa: "Bu kontakt allaqachon mavjud. Yangilaysizmi?"

## 🔴 Qiyin (+20 XP)
- Qidiruv qisman bo'lsin: "az" yozilsa, "Aziz" va "Nazira" topilsin (katta-kichik harfga e'tiborsiz).
- Telefon raqami 7-darsdagi kabi tozalansin va tekshirilsin.
- **Statistika:** har bir guruhda nechta kontakt bor (dict comprehension yoki `Counter`)? Nechta kontaktda email yo'q?
- Barcha guruhlar ro'yxatini set orqali chiqaring.

Namuna: `kod/kontaktlar_v1.py`
