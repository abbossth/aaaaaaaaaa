# 33-dars slaydlari: Massiv va obyekt 📦

## 1-slayd
**25 ta o'zgaruvchi? Yo'q — 1 ta massiv!**

## 2-slayd — Massiv = poyezd 🚃
```js
const mevalar = ["olma", "nok", "uzum"];
//                  0       1      2     ← indeks (0 dan!)
mevalar[0];          // "olma"
mevalar.length;      // 3
mevalar.push("anor");     // oxiriga qo'shish
mevalar.pop();            // oxiridan olish
mevalar.includes("nok");  // true
```

## 3-slayd — Aylanib chiqish
```js
for (const meva of mevalar) {
  console.log(meva);
}
```

## 4-slayd — Obyekt = kartochka 🪪
```js
const oquvchi = {
  ism: "Aziz",
  yosh: 14,
  sinf: "8.10",
};
oquvchi.ism;          // "Aziz"
oquvchi.yosh = 15;    // o'zgartirish
```

## 5-slayd — Obyektlar massivi
```js
const sinf = [
  { ism: "Aziz", ball: 87 },
  { ism: "Malika", ball: 95 },
];
for (const o of sinf) console.log(`${o.ism}: ${o.ball}`);
```

## 6-slayd — Sehrli metodlar ✨
`filter` — tanlash · `map` — o'zgartirish · `find` — birinchisini topish
```js
const alochilar = sinf.filter((o) => o.ball >= 86);
const ismlar = sinf.map((o) => o.ism);
```
