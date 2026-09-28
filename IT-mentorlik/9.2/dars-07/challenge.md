# 7-dars challenge: "Ma'lumot tozalovchi" 🧹

**Vaqt:** 17 daqiqa | **Format:** juftlik

Sizga ro'yxatdan o'tish formasidan kelgan "iflos" ma'lumotlar berildi (`kod/iflos.txt`). Har bir qatorda: `ism;email;telefon` bor. Dastur har bir qatorni o'qib, tozalashi va chiroyli jadval ko'rinishida chiqarishi kerak.

## Qoidalar
- **Ism:** ortiqcha probelsiz, har bir so'z bosh harf bilan (`"  aZIZ   karimov "` → `"Aziz Karimov"`)
- **Email:** kichik harf, probelsiz. Noto'g'ri bo'lsa (`@` yo'q), `❌ noto'g'ri` deb yozilsin.
- **Telefon:** faqat raqamlar, `998` bilan boshlanishi va 12 raqamdan iborat bo'lishi kerak. `90 123 45 67` → `998901234567`. Formatlangan holda chiqarilsin: `+998 90 123-45-67`.

Hozircha fayl o'qish o'tilmagan. Shuning uchun ma'lumotlarni ko'p qatorli satrga joylang va `.split("\n")` bilan qatorlarga ajrating.

**XP:** barcha qatorlarni to'g'ri tozalagan birinchi 3 juftlik: +30/+20/+10.
