# 17-dars slaydlari: DOM

## 1-slayd
🌳 **DOM = HTML'ning JavaScript'dagi daraxti**

## 2-slayd — Daraxt
```
document
 └─ html
     ├─ head
     │   └─ title
     └─ body
         ├─ h1
         └─ ul
             ├─ li
             └─ li
```

## 3-slayd — Topish 🔍
```js
document.getElementById("sarlavha");
document.querySelector(".karta");          // birinchisi
document.querySelectorAll(".karta");       // hammasi (NodeList)
```

## 4-slayd — O'zgartirish ✏️
```js
el.textContent = "Yangi matn";              // xavfsiz
el.innerHTML = "<b>Qalin</b> matn";          // HTML bilan
el.style.color = "red";
el.classList.add("faol");                  // ✅ stilni CSS'da saqlash yaxshiroq
el.classList.toggle("qorongi");
el.setAttribute("src", "rasm.png");
```

## 5-slayd — Yaratish ➕
```js
const li = document.createElement("li");
li.textContent = "Yangi element";
ro'yxat.append(li);
li.remove();
```

## 6-slayd — Ma'lumotdan render 🎨
```js
const mevalar = ["🍎 Olma", "🍐 Nok", "🍇 Uzum"];
ul.innerHTML = mevalar.map((m) => `<li>${m}</li>`).join("");
```

## 7-slayd — ⚠️ innerHTML va xavfsizlik
Foydalanuvchi kiritgan matnni `innerHTML` ga qo'ymang! → XSS hujumi
✅ Foydalanuvchi matni uchun `textContent`
