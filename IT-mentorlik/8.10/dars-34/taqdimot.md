# 34-dars slaydlari: DOM 🌳

## 1-slayd
🙃 `document.body.style.transform = "rotate(180deg)"` — sahifa ag'darildi!

## 2-slayd — DOM = Document Object Model
```
document
 └─ html
     ├─ head → title
     └─ body
         ├─ h1#sarlavha
         ├─ p.matn
         └─ ul#royxat → li, li, li
```
Har bir teg — JavaScript uchun **obyekt** 📦

## 3-slayd — Topish 🔍
```js
document.getElementById("sarlavha")     // id bo'yicha
document.querySelector(".matn")         // birinchi mos keladigan (CSS selektor)
document.querySelectorAll("li")         // hammasi (ro'yxat)
```

## 4-slayd — O'zgartirish ✏️
```js
sarlavha.textContent = "Salom!";            // faqat matn
matn.innerHTML = "<b>Qalin</b> matn";      // HTML bilan
sarlavha.style.color = "red";               // stil (CSS: font-size → JS: fontSize)
rasm.src = "mushuk.jpg";                    // atribut
karta.classList.add("faol");                // klass: add / remove / toggle
```

## 5-slayd — Yaratish ➕
```js
const li = document.createElement("li");    // 1. yaratish
li.textContent = "Minecraft";               // 2. to'ldirish
royxat.append(li);                          // 3. sahifaga qo'shish
```

## 6-slayd — Massiv → sahifa 🔁
```js
for (const oyin of oyinlar) {
  const li = document.createElement("li");
  li.textContent = oyin;
  royxat.append(li);
}
```

## 7-slayd — Qoida
`<script src="app.js">` — `</body>` dan **oldin** (aks holda JS elementlarni topa olmaydi → `null`)
