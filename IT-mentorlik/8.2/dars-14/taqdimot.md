# 14-dars slaydlari: Funksiyalar

## 1-slayd
🧃 **Funksiya = blender:** kirish → ish → chiqish

## 2-slayd — 3 usul
```js
function kvadrat(x) { return x * x; }          // declaration
const kvadrat2 = function (x) { return x * x; }; // expression
const kvadrat3 = (x) => x * x;                   // arrow ✨
```

## 3-slayd — Parametr va default
```js
function salom(ism = "mehmon") {
  return `Salom, ${ism}!`;
}
salom("Aziz");   // "Salom, Aziz!"
salom();         // "Salom, mehmon!"
```

## 4-slayd — return vs console.log
```js
const a = (x) => { console.log(x * 2); };   // chiqaradi, lekin QAYTARMAYDI
const b = (x) => x * 2;                     // qaytaradi
a(5) + 1;   // NaN (undefined + 1)
b(5) + 1;   // 11 ✅
```

## 5-slayd — Scope
```js
const global = "hamma ko'radi";
function f() {
  const lokal = "faqat f ichida";
  if (true) { let blok = "faqat if ichida"; }
}
```

## 6-slayd — Callback
```js
setTimeout(() => alert("3 soniya o'tdi!"), 3000);
tugma.addEventListener("click", () => alert("Bosildi!"));   // 18-dars!
```
