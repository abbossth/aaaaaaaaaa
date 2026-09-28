# 35-dars slaydlari: Eventlar ⚡

## 1-slayd
🌙 ↔ ☀️ — bitta tugma, butun sahifa o'zgaradi

## 2-slayd — Event = hodisa
🖱 `click` · ⌨️ `keydown` · ✍️ `input` · 📨 `submit` · 🖱 `mouseover` · 📜 `scroll`

## 3-slayd — Formula
```js
element.addEventListener("click", () => {
  // bosilganda nima bo'lsin
});
```
**Kim?** (element) + **Qachon?** (event) + **Nima?** (funksiya)

## 4-slayd — Hisoblagich
```js
let son = 0;                                   // holat
plus.addEventListener("click", () => {
  son++;                                       // 1. holatni o'zgartir
  sonEl.textContent = son;                     // 2. ekranni yangila
});
```

## 5-slayd — Dark mode 🌙
```css
body.qorongi { background: #111; color: #fff; }
```
```js
btn.addEventListener("click", () => {
  document.body.classList.toggle("qorongi");   // bor bo'lsa olib tashlaydi, yo'q bo'lsa qo'shadi
});
```

## 6-slayd — event obyekti
```js
document.addEventListener("keydown", (event) => {
  console.log(event.key);    // "a", "Enter", "ArrowUp"...
});
input.addEventListener("input", () => {
  console.log(input.value);  // yozilgan matn
});
```

## 7-slayd — ⚠️ Xato
```js
btn.addEventListener("click", salom());   // ❌ darhol chaqiriladi
btn.addEventListener("click", salom);     // ✅ bosilganda chaqiriladi
```
