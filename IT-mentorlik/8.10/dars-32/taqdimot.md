# 32-dars slaydlari: Funksiyalar 🧃

## 1-slayd
**Funksiya = blender:** meva → 🧃

## 2-slayd — Funksiya yaratish va chaqirish
```js
function salom(ism) {          // ism — parametr
  return `Salom, ${ism}!`;
}
salom("Aziz");                 // "Aziz" — argument
```

## 3-slayd — return
```js
function kvadrat(x) {
  return x * x;
}
const natija = kvadrat(5) + 1;   // 26
```
`return` — natijani **qaytaradi** · `console.log` — faqat **ko'rsatadi**

## 4-slayd — Arrow funksiya ✨
```js
const kvadrat = (x) => x * x;
const salom = (ism = "mehmon") => `Salom, ${ism}!`;
```

## 5-slayd — Tugma + funksiya
```html
<button onclick="salomBer()">Bos meni</button>
<script>
  function salomBer() {
    alert("Salom! 👋");
  }
</script>
```
(Keyingi darslarda chiroyliroq usul: `addEventListener`)
