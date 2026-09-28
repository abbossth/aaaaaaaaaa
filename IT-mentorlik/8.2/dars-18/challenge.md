# 18-dars challenge: "Klaviatura pianinosi" 🎹

**Vaqt:** 17 daqiqa | **Format:** juftlik

Klaviatura tugmalari bosilganda nota chalinadigan pianino yarating!

## Talablar
1. Sahifada 7 ta "klavish" (div): A S D F G H J harflari yozilgan.
2. Klaviaturadagi tegishli harf bosilganda (`keydown`) klavish yonadi (`classList.add("bosilgan")`) va 150 ms dan keyin o'chadi (`setTimeout`).
3. Ovoz: Web Audio API bilan (kodni `kod/ovoz.js` dan oling va tushunib ishlating):
```js
function chal(chastota) {
  const ctx = new AudioContext();
  const osc = ctx.createOscillator();
  osc.frequency.value = chastota;
  osc.connect(ctx.destination);
  osc.start();
  osc.stop(ctx.currentTime + 0.3);
}
// Do Re Mi Fa Sol Lya Si: 262 294 330 349 392 440 494
```
4. Sichqoncha bilan bosganda ham ishlasin (`click`).

**Bonus (+10 XP):** "Qo'shiq yozish" rejimi: bosilgan notalar massivga yoziladi va "▶ Chalish" tugmasi ularni ketma-ket chaladi.

**XP:** ishlaydigan birinchi 3 juftlik +30/+20/+10
