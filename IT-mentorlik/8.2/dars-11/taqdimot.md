# 11-dars slaydlari: JavaScript asoslari

## 1-slayd
🧠 **JavaScript — sahifaning miyasi**

## 2-slayd — JS'ni ulash
```html
<body>
  ...
  <script src="app.js"></script>   <!-- body oxirida -->
</body>
```
yoki `<head>` da: `<script src="app.js" defer></script>`

## 3-slayd — O'zgaruvchilar
```js
let yosh = 14;          // o'zgarishi mumkin
const ism = "Aziz";     // o'zgarmas
yosh = 15;              // ✅
ism = "Bobur";          // 💥 TypeError
```
`var` — eski usul, ishlatmang
Nomlash: **camelCase** → `userName`, `totalPrice`

## 4-slayd — Ma'lumot turlari
`"Salom"` string · `42`, `3.14` number · `true/false` boolean
`undefined` qiymat berilmagan · `null` ataylab bo'sh · `{}`, `[]` object
`typeof 42` → `"number"`

## 5-slayd — Operatorlar
`+ - * / % **` · `++ --` · `+= -=`
`> < >= <=` · `=== !==` (qat'iy) · `&& || !`

## 6-slayd — ⚠️ == va ===
```js
5 == "5"    // true  😱 (turni o'zgartiradi)
5 === "5"   // false ✅ (tur ham tekshiriladi)
```
**Qoida: doim `===` ishlating!**

## 7-slayd — Template literal
```js
const ism = "Aziz", yosh = 14;
console.log(`Salom, ${ism}! Keyingi yil ${yosh + 1} yoshda bo'lasiz.`);
```

## 8-slayd — Turlarni o'zgartirish
```js
const javob = prompt("Yoshingiz?");   // doim string!
const yosh = Number(javob);
"5" + 5    // "55"   (satrga qo'shadi)
"5" - 5    // 0      (songa aylantiradi)
```
