# 16-dars. Obyektlar va JSON

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- Obyekt yaratadi (kalit: qiymat), xossalarni o'qiydi (`obj.key`, `obj["key"]`), qo'shadi, o'zgartiradi va o'chiradi.
- Obyekt ichida metod yozadi va `this` ning oddiy holatini tushunadi.
- `Object.keys/values/entries`, `for...in`, destructuring (`const { ism, yosh } = user`) va spread (`{...obj}`) ni ishlatadi.
- Massiv ichidagi obyektlar (real ma'lumotlar) bilan ishlaydi.
- JSON nima ekanini, `JSON.stringify` va `JSON.parse` ni biladi. `localStorage` ga saqlash asoslari.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Brauzerda `https://api.github.com/users/torvalds`. *"Bu JSON. Internetdagi barcha ilovalar shu 'til'da gaplashadi. JS obyektiga juda o'xshaydi, to'g'rimi?"* |
| 5–10 | **Takrorlash** | 15-dars testi |
| 10–28 | **Yangi mavzu** | Obyekt yaratish/o'qish/o'zgartirish. Metodlar. Keys/values/entries. Destructuring, spread. Ichma-ich obyekt. JSON, stringify/parse. localStorage |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md`: "Kontaktlar kitobi" ma'lumotlari |
| 55–72 | **Challenge** | `challenge.md`: "API detektivi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```js
const user = {
  ism: "Aziz",
  yosh: 14,
  qiziqishlar: ["futbol", "JS"],
  manzil: { shahar: "Toshkent", tuman: "Chilonzor" },
  salom() { return `Salom, men ${this.ism}!`; },
};

user.sinf = "8.2";
user.yosh++;
delete user.qiziqishlar;
console.log(user.manzil.shahar, user["ism"], user.salom());

const { ism, yosh } = user;
const nusxa = { ...user, ism: "Bobur" };

for (const [kalit, qiymat] of Object.entries(user)) console.log(kalit, qiymat);

const json = JSON.stringify(user);
const qayta = JSON.parse(json);
localStorage.setItem("user", json);
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
