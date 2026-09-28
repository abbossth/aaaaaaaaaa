# 13-dars. Sikllar: for, while, for...of

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- `for`, `while`, `do...while` va `for...of` sikllarini yozadi va qaysi birini qachon ishlatishni biladi.
- `break` va `continue` bilan siklni boshqaradi.
- Hisoblagich va yig'uvchi o'zgaruvchilar bilan masalalar yechadi.
- Cheksiz sikl xavfini tushunadi va undan qochadi.
- Sikl bilan HTML yaratadi (`document.write` o'rniga `innerHTML`, DOM'ga kirish).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Sahifada 1 dan 1000 gacha raqamlangan tugmalar kerak. Qo'lda yozasizmi?"* 3 qatorlik sikl → sahifada 1000 ta tugma 🤯 |
| 5–10 | **Takrorlash** | 12-dars testi |
| 10–25 | **Yangi mavzu** | for (3 qism), while, do...while, for...of (satr/massiv), break/continue. Flowgorithm sikllari bilan taqqoslash |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Son topish" o'yini |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```js
for (let i = 1; i <= 5; i++) {
  console.log(`${i}-qadam`);
}

let parol = "";
while (parol !== "js2026") {
  parol = prompt("Parol:");
}

for (const harf of "Salom") console.log(harf);

let html = "";
for (let i = 1; i <= 1000; i++) html += `<button>${i}</button>`;
document.body.innerHTML = html;
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
