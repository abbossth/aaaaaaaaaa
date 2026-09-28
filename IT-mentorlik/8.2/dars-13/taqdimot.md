# 13-dars slaydlari: Sikllar

## 1-slayd
🔁 **1000 ta tugmani 3 qatorda!**

## 2-slayd — for
```js
for (let i = 0; i < 5; i++) { ... }
//   boshlanish; shart;  qadam
```

## 3-slayd — while va do...while
```js
while (shart) { ... }          // avval tekshiradi
do { ... } while (shart);      // kamida 1 marta bajaradi
```

## 4-slayd — for...of
```js
for (const meva of ["olma", "nok"]) console.log(meva);
for (const harf of "JS") console.log(harf);
```

## 5-slayd — break va continue
`break` — sikldan chiqish 🚪 · `continue` — keyingi aylanishga o'tish ⏭
```js
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) continue;   // juftlarni o'tkazib yubor
  if (i > 7) break;            // 7 dan keyin to'xta
  console.log(i);              // 1 3 5 7
}
```

## 6-slayd — ⚠️ Cheksiz sikl
```js
let i = 0;
while (i < 10) { console.log(i); }   // i o'zgarmaydi → brauzer qotadi!
```
Qotib qolsa: tabni yopish yoki Chrome'da `Shift+Esc` → Task Manager
