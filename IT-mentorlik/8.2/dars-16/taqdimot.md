# 16-dars slaydlari: Obyektlar va JSON

## 1-slayd
📦 **Obyekt = kalit: qiymat juftliklari**

## 2-slayd — Yaratish va o'qish
```js
const kitob = { nom: "O'tkan kunlar", muallif: "A. Qodiriy", yil: 1926 };
kitob.nom;            // "O'tkan kunlar"
kitob["muallif"];     // "A. Qodiriy"
kitob.janr = "roman"; // qo'shish
delete kitob.yil;     // o'chirish
```

## 3-slayd — Metod va this
```js
const mashina = {
  marka: "Chevrolet",
  tezlik: 0,
  gaz() { this.tezlik += 10; return this.tezlik; },
};
```

## 4-slayd — Aylanib chiqish
```js
Object.keys(kitob);    // ["nom", "muallif", ...]
Object.values(kitob);  // ["O'tkan kunlar", ...]
Object.entries(kitob); // [["nom", "..."], ...]
```

## 5-slayd — Destructuring va spread ✨
```js
const { nom, muallif } = kitob;
const yangi = { ...kitob, yil: 2026 };   // nusxa + o'zgartirish
```

## 6-slayd — JSON
```js
JSON.stringify(obj);   // obyekt → satr (yuborish/saqlash uchun)
JSON.parse(satr);      // satr → obyekt
```
JSON'da: kalitlar **qo'shtirnoqda**, funksiya va `undefined` yo'q

## 7-slayd — localStorage 💾
```js
localStorage.setItem("todos", JSON.stringify(todos));
const todos = JSON.parse(localStorage.getItem("todos")) || [];
```
Brauzer yopilsa ham ma'lumot qoladi!
