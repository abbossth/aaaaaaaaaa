# 36-dars slaydlari: Forma va localStorage 💾

## 1-slayd
😢 Sahifani yangiladim — hammasi yo'qoldi!

## 2-slayd — submit eventi
```js
forma.addEventListener("submit", (event) => {
  event.preventDefault();      // ⚠️ busiz sahifa yangilanadi
  // tekshirish...
});
```

## 3-slayd — Validatsiya = "qo'riqchi" 💂
| Maydon | Qoida | Kod |
|---|---|---|
| Ism | ≥ 2 harf | `ism.length >= 2` |
| Yosh | 10–18 | `yosh >= 10 && yosh <= 18` |
| Telefon | +998 bilan, 13 belgi | `tel.startsWith("+998") && tel.length === 13` |

## 4-slayd — Xatoni chiroyli ko'rsatish
🔴 qizil ramka + matn → foydalanuvchi **nimani** tuzatishni biladi

## 5-slayd — localStorage = brauzer "cho'ntagi" 👖
```js
localStorage.setItem("ism", "Aziz");     // saqlash
localStorage.getItem("ism");             // "Aziz" — yangilasangiz ham!
localStorage.removeItem("ism");          // o'chirish
```
F12 → Application → Local Storage 👀

## 6-slayd — Faqat MATN saqlanadi!
```js
const vazifalar = [{ matn: "Uy ishi", bajarildi: false }];
localStorage.setItem("vazifalar", JSON.stringify(vazifalar));   // massiv → matn
const qaytgan = JSON.parse(localStorage.getItem("vazifalar"));  // matn → massiv
```

## 7-slayd — To-Do sxemasi 🔁
```
[ massiv (holat) ] → saqla() → localStorage
        ↓
      chiz() → sahifa
        ↑
   click/submit
```
