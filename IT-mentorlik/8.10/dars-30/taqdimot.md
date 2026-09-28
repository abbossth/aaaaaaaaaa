# 30-dars slaydlari: Shartlar 🔀

## 1-slayd
**Kompyuter qaror qabul qiladi: AGAR ... BO'LSA**

## 2-slayd — Operatorlar
➕ `+ - * /` · `%` qoldiq (`7 % 2 = 1`) · `**` daraja
⚖️ `>` `<` `>=` `<=` `===` (teng) `!==` (teng emas)
🔗 `&&` VA · `||` YOKI · `!` EMAS

## 3-slayd — ⚠️ == va ===
```js
5 == "5"    // true  😱
5 === "5"   // false ✅
```
**Doim `===` ishlating!**

## 4-slayd — if / else (Flowgorithm'dagi romb!)
```js
const yosh = Number(prompt("Yoshingiz?"));
if (yosh >= 18) {
  alert("Siz kattasiz");
} else {
  alert("Siz hali yoshsiz");
}
```

## 5-slayd — else if
```js
if (ball >= 86) {
  alert("5 — A'lo! 🏆");
} else if (ball >= 71) {
  alert("4 — Yaxshi 👍");
} else if (ball >= 56) {
  alert("3 — Qoniqarli");
} else {
  alert("2 — Harakat qil! 💪");
}
```
**Kattadan kichikka tekshiring!**

## 6-slayd — switch
```js
switch (kun) {
  case "shanba":
  case "yakshanba":
    alert("Dam olish! 🎉");
    break;
  default:
    alert("Maktabga! 📚");
}
```
