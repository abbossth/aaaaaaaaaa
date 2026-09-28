# 15-dars slaydlari: Massivlar

## 1-slayd
🛍 **Uzum filtrlari = `filter` + `sort`**

## 2-slayd — Massiv
```js
const mevalar = ["olma", "nok", "uzum"];
mevalar[0];        // "olma"
mevalar.length;    // 3
mevalar.push("anor");       // oxiriga
mevalar.pop();              // oxiridan olib tashlash
mevalar.includes("nok");    // true
```

## 3-slayd — Sehrli metodlar (emojida) 🍔
```
map:     [🐄, 🥔, 🐔].map(pishir)        → [🍔, 🍟, 🍗]
filter:  [🍔, 🍟, 🍗].filter(vegetarian) → [🍟]
find:    [🍔, 🍟, 🍗].find(tovuq)        → 🍗
reduce:  [🍔, 🍟, 🍗].reduce(ye)         → 💩 😄
```

## 4-slayd — map
```js
const narxlar = [10000, 25000, 5000];
const qqsBilan = narxlar.map((n) => n * 1.12);
```

## 5-slayd — filter va find
```js
const qimmat = narxlar.filter((n) => n > 8000);   // [10000, 25000]
const birinchi = narxlar.find((n) => n > 8000);   // 10000
```

## 6-slayd — reduce
```js
const jami = narxlar.reduce((yigindi, n) => yigindi + n, 0);   // 40000
```

## 7-slayd — Zanjir ⛓
```js
mahsulotlar
  .filter((m) => m.narx < 500000)
  .sort((a, b) => a.narx - b.narx)
  .map((m) => m.nom);
```

## 8-slayd — ⚠️ sort tuzog'i
```js
[10, 1, 5, 100].sort();                  // [1, 10, 100, 5] 😱 (satr sifatida!)
[10, 1, 5, 100].sort((a, b) => a - b);   // [1, 5, 10, 100] ✅
```
