# 12-dars slaydlari: Shartlar

## 1-slayd
🔀 **Agar... bo'lsa... aks holda...**

## 2-slayd — if / else if / else
```js
if (harorat > 30) {
  console.log("Issiq 🥵");
} else if (harorat > 15) {
  console.log("Iliq 😊");
} else {
  console.log("Sovuq 🥶");
}
```

## 3-slayd — Mantiqiy operatorlar
`&&` VA · `||` YOKI · `!` EMAS
```js
if (yosh >= 13 && roziligiBor) { ... }
```

## 4-slayd — switch
```js
switch (tanlov) {
  case "1": console.log("Choy"); break;
  case "2": console.log("Qahva"); break;
  default: console.log("Noma'lum");
}
```
❗ `break` unutilsa, keyingi case ham bajariladi!

## 5-slayd — Ternar operator
```js
const natija = ball >= 56 ? "O'tdi ✅" : "O'tmadi ❌";
```

## 6-slayd — Truthy / Falsy
Falsy: `false`, `0`, `""`, `null`, `undefined`, `NaN`
Qolganlari — truthy (hatto `"0"` va `[]` ham!)
```js
if (ism) { ... }   // ism bo'sh bo'lmasa
```
