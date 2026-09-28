# 16-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. O'zingiz haqingizda obyekt: ism, yosh, sinf, qiziqishlar (massiv), manzil (ichma-ich obyekt), `tanishtir()` metodi.
2. `Object.entries` bilan barcha xossalarni `kalit: qiymat` ko'rinishida chiqaring.

## 🟡 O'rta (+10 XP): Kontaktlar
3. `kontaktlar` massivi: 5 ta obyekt `{ id, ism, tel, guruh }`.
4. Funksiyalar: `qoshish(ism, tel, guruh)`, `topish(ism)` (`find`), `guruhBoyicha(guruh)` (`filter`), `ochirish(id)` (`filter` bilan yangi massiv).
5. Kontaktlarni `localStorage` ga saqlang va sahifa yangilanganda qayta yuklang.

## 🔴 Qiyin (+20 XP)
6. `guruhlash(kontaktlar)` → `{ dost: [...], oila: [...], sinfdosh: [...] }` (`reduce`).
7. Kontaktlarni JSON fayl sifatida yuklab olish tugmasi:
```js
const blob = new Blob([JSON.stringify(kontaktlar, null, 2)], { type: "application/json" });
const a = document.createElement("a");
a.href = URL.createObjectURL(blob);
a.download = "kontaktlar.json";
a.click();
```
