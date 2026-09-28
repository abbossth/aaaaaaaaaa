# 31-dars slaydlari: Sikllar 🔁

## 1-slayd — 1000 ta tugma, 3 qator!
```js
let html = "";
for (let i = 1; i <= 1000; i++) html += `<button>${i}</button>`;
document.body.innerHTML = html;
```

## 2-slayd — for (Flowgorithm'dagi For!)
```js
for (let i = 1; i <= 5; i++) {
  console.log(i);          // 1 2 3 4 5
}
```
`let i = 1` — boshlanish · `i <= 5` — shart · `i++` — qadam

## 3-slayd — Yig'uvchi
```js
let summa = 0;
for (let i = 1; i <= 100; i++) {
  summa += i;              // summa = summa + i
}
console.log(summa);        // 5050
```

## 4-slayd — while (shart bajarilguncha)
```js
let parol = "";
while (parol !== "js2026") {
  parol = prompt("Parol:");
}
alert("Xush kelibsiz!");
```

## 5-slayd — break va continue
`break` — sikldan chiqish 🚪 · `continue` — keyingi aylanishga ⏭

## 6-slayd — ⚠️ Cheksiz sikl
Sikl ichida shart hech qachon `false` bo'lmasa → brauzer qotadi!
Qotsa: tabni yoping (`Ctrl+W`)
