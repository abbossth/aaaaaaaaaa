# 12-dars slaydlari: Factory va Singleton

## 1-slayd
🏭 **Factory** va ☝️ **Singleton**

## 2-slayd — Design pattern nima?
Tez-tez uchraydigan muammoning **sinalgan yechimi** (retsept).
"Gang of Four" kitobi (1994): 23 ta andoza
🏗 Yaratuvchi · 🧱 Tuzilmaviy · 🎭 Xulq-atvor

## 3-slayd — Factory: muammo
```js
// ❌ bu if'lar 10 ta faylda takrorlanadi
let n;
if (type === "sms") n = new SmsNotification(to);
else if (type === "email") n = new EmailNotification(to);
else if (type === "telegram") n = new TelegramNotification(to);
```

## 4-slayd — Factory: yechim
```js
const creators = { sms: SmsNotification, email: EmailNotification, telegram: TelegramNotification };

export function createNotification(type, to) {
  const Creator = creators[type];
  if (!Creator) throw new Error(`Noma'lum tur: ${type}`);
  return new Creator(to);
}
// Mijoz kodi:
createNotification(user.preferredChannel, user.contact).send("Salom!");
```
✅ Yangi tur = bitta qator (OCP!) · ✅ Mijoz aniq klasslarni bilmaydi

## 5-slayd — Singleton
**Butun tizimda bitta nusxa:** logger, sozlamalar, DB ulanishlar puli
```js
class Logger {
  static #instance;
  static getInstance() { return (Logger.#instance ??= new Logger()); }
}
Logger.getInstance() === Logger.getInstance(); // true
```

## 6-slayd — JS'dagi "bepul" singleton
```js
// logger.js
class Logger { ... }
export const logger = new Logger();   // modul faqat bir marta yuklanadi
```

## 7-slayd — ⚠️ Singleton'ning qorong'u tomoni
- Yashirin global holat
- Test qilish qiyin (holat testlar orasida "oqib" o'tadi)
- Kuchli bog'liqlik (DIP buziladi)
➡️ Kamdan-kam va ongli ravishda ishlating. Ko'pincha DI (konstruktor orqali berish) yaxshiroq.
