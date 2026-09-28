# 18-dars slaydlari: Eventlar

## 1-slayd
🖱 **Foydalanuvchi harakat qiladi → sahifa javob beradi**

## 2-slayd — addEventListener
```js
const tugma = document.querySelector("#tugma");
tugma.addEventListener("click", () => {
  alert("Bosildi!");
});
```

## 3-slayd — Event turlari
🖱 `click` `dblclick` `mouseover` · ⌨️ `keydown` `keyup`
📝 `input` (har bir harf) · `change` (tanlov o'zgarganda) · `submit` (forma)
📄 `DOMContentLoaded` · `scroll` · `resize`

## 4-slayd — event obyekti
```js
input.addEventListener("input", (e) => {
  console.log(e.target.value);   // kiritilgan matn
});
document.addEventListener("keydown", (e) => {
  console.log(e.key);            // "a", "Enter", "ArrowUp"
});
```

## 5-slayd — Forma: preventDefault
```js
form.addEventListener("submit", (e) => {
  e.preventDefault();            // sahifa yangilanmasin!
  const ism = form.ism.value.trim();
  if (!ism) return alert("Ism kiriting");
});
```

## 6-slayd — Event delegation
```js
// 100 ta tugmaga 100 ta listener o'rniga — ota elementga bitta:
ro'yxat.addEventListener("click", (e) => {
  if (e.target.matches(".ochirish")) e.target.closest("li").remove();
});
```
