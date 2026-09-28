# 12-dars. Shart operatorlari: if/else, switch, ternary

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- `if / else if / else` va ichma-ich shartlarni yozadi.
- `switch` bilan ko'p variantli tanlovni qiladi (`break` ning ahamiyati).
- Ternar operator (`shart ? a : b`) bilan qisqa shart yozadi.
- Truthy/falsy qiymatlarni (`0, "", null, undefined, NaN, false`) biladi.
- Real vazifalarni yechadi: baho, kalkulyator, "Tosh-qaychi-qog'oz" g'olibi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Instagram 13 yoshdan kichiklarni qanday qilib ro'yxatdan o'tkazmaydi? Telegram'da 'o'qildi' belgisi qachon ko'k bo'ladi?"* Hammasi `if`! |
| 5–10 | **Takrorlash** | 11-dars testi |
| 10–25 | **Yangi mavzu** | if/else if/else (Flowgorithm'dagi romb bilan taqqoslash), mantiqiy operatorlar, switch, ternar, truthy/falsy |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Tosh-qaychi-qog'oz" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```js
const ball = Number(prompt("Ball (0-100):"));

if (isNaN(ball) || ball < 0 || ball > 100) {
  alert("Noto'g'ri ball!");
} else if (ball >= 86) {
  alert("A'lo — 5 🏆");
} else if (ball >= 71) {
  alert("Yaxshi — 4 👍");
} else if (ball >= 56) {
  alert("Qoniqarli — 3");
} else {
  alert("Qoniqarsiz — 2 😢");
}

const kun = prompt("Hafta kuni:").toLowerCase();
switch (kun) {
  case "shanba":
  case "yakshanba":
    console.log("Dam olish kuni 🎉");
    break;
  default:
    console.log("Ish kuni 📚");
}

const yosh = 15;
const status = yosh >= 18 ? "katta" : "yosh";
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
