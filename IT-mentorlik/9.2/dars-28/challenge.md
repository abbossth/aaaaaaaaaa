# 28-dars challenge: "Jadval shifokori" 🩺

**Vaqt:** 15 daqiqa | **Format:** jamoalar

Quyidagi "kasal" jadvalni "davolang" (normalizatsiya qiling):

| buyurtma_id | sana | mijoz_ism | mijoz_tel | mijoz_manzil | mahsulotlar | narxlar | jami |
|---|---|---|---|---|---|---|---|
| 1 | 01.10 | Aziz | 901234567 | Chilonzor 5 | Non, Sut | 4000, 12000 | 16000 |
| 2 | 01.10 | Malika | 907654321 | Yunusobod 3 | Choy | 15000 | 15000 |
| 3 | 02.10 | Aziz | 901234567 | Chilonzor 5 | Non, Non, Choy | 4000, 4000, 15000 | 23000 |

## Savollar
1. Qanday "kasalliklar" bor? (Kamida 4 ta: takrorlanish, bitta katakda bir nechta qiymat, hisoblanadigan maydon saqlanishi...)
2. Aziz telefonini o'zgartirsa, nechta joyni tuzatish kerak?
3. Sog'lom jadvallar tuzilmasini chizing (PK/FK bilan).

**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5

<details><summary>Javob (mentor uchun)</summary>

- Kasalliklar: mijoz ma'lumotlari takrorlanadi (update anomaliyasi); `mahsulotlar` va `narxlar` da bir katakda bir nechta qiymat (1NF buzilgan); `jami` hisoblanadigan maydon; mahsulot narxi har buyurtmada takror.
- Aziz telefoni: 2 joyda (ko'p buyurtmada — ko'p joyda).
- Yechim: `mijozlar(id, ism, tel, manzil)`, `mahsulotlar(id, nom, narx)`, `buyurtmalar(id, sana, mijoz_id FK)`, `buyurtma_qatorlari(buyurtma_id FK, mahsulot_id FK, soni, narx)`. (Qatorda narx saqlanadi — sotuv paytidagi narx tarix uchun!)
</details>
