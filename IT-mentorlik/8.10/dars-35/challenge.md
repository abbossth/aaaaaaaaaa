# 35-dars challenge: "Tez barmoqlar" ⚡👆

**Vaqt:** 17 daqiqa (10 daqiqa yasash + 7 daqiqa turnir) | **Format:** individual

## Yasash
10 soniyada tugmani necha marta bosa olasiz?
- "Boshlash" tugmasi → 10 soniya taymer (`setTimeout(() => {...}, 10000)`)
- Taymer davomida katta tugmani bosish — `son++`
- Vaqt tugagach: tugma o'chadi (`btn.disabled = true`), natija chiqadi: "Siz 10 soniyada 57 marta bosdingiz!"

Maslahat:
```js
let oyinBormi = false;
boshlaBtn.addEventListener("click", () => {
  son = 0; oyinBormi = true;
  setTimeout(() => { oyinBormi = false; natija.textContent = `Natija: ${son}`; }, 10000);
});
bosBtn.addEventListener("click", () => { if (oyinBormi) son++; });
```

## Turnir
Hamma o'z o'yinida 3 marta o'ynaydi → eng yaxshi natija doskaga. 🏆

**XP:** ishlaydigan o'yin +10 · sinf rekordi +10 · qo'shimcha funksiya (rekordni eslab qolish, animatsiya) +5
