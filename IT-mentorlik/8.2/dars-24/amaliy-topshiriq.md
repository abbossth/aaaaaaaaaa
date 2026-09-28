# Oraliq nazorat #1 — amaliy qism (60 ball, 30 daqiqa)

**Qoidalar:** AI va qidiruv taqiqlanadi. Faqat MDN (developer.mozilla.org) va o'z eski fayllaringiz. `nazorat1-familiya/` papkasida `index.html`, `style.css`, `app.js`.

## Vazifa: "Sinf reytingi" sahifasi

`app.js` ga quyidagi massivni qo'ying:
```js
const oquvchilar = [
  { ism: "Aziz", ball: 87 }, { ism: "Malika", ball: 95 }, { ism: "Bobur", ball: 72 },
  { ism: "Dilnoza", ball: 91 }, { ism: "Sardor", ball: 64 }, { ism: "Nigora", ball: 78 },
];
```

### 🟢 1-qism (20 ball): HTML/CSS
- Semantik skelet: `header` (sarlavha), `main`, `footer`
- Kartochkalar Grid bilan: kompyuterda 3 ustun, telefonda 1 ustun (media query)
- Kartochka: oq fon, radius, soya, hover'da ko'tariladi (transition)

### 🟡 2-qism (20 ball): JS render
- Massivdan kartochkalarni **JS bilan** chizing: ism, ball, baho (86+ → 5, 71+ → 4, 56+ → 3, qolgani → 2)
- Kartochkalar ball bo'yicha kamayish tartibida
- TOP-3 ga 🥇🥈🥉 belgisi
- Sahifa tepasida: sinf o'rtacha bali (`reduce`)

### 🔴 3-qism (20 ball): Interaktivlik
- Qidiruv input'i: ism bo'yicha jonli filtr (`input` eventi)
- Forma: yangi o'quvchi qo'shish (ism + ball). Validatsiya: ism bo'sh emas, ball 0..100. Xato bo'lsa, qizil xabar
- Qo'shilgan o'quvchilar `localStorage` da saqlansin

Namuna yechim (faqat mentor uchun): `kod/yechim/`
