# 12-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
`kod/factory.js` va `kod/singleton.js` ni ishga tushiring. Factory'ga **"push"** bildirishnomasini qo'shing (`PushNotification`). Qaysi qatorlarni o'zgartirdingiz? Mijoz kodi o'zgardimi?

## 🟡 O'rta (+10 XP): Shakllar fabrikasi
`createShape(config)` fabrikasi: `{ type: "circle", r: 5 }`, `{ type: "rect", w: 2, h: 3 }`, `{ type: "triangle", a: 3, b: 4, c: 5 }` dan tegishli obyektni yaratsin. Har bir shaklda `area()` va `perimeter()` bo'lsin (LSP!). JSON massividan 10 ta shakl yaratib, umumiy yuzani hisoblang. Vitest bilan 5 ta test yozing.

## 🔴 Qiyin (+20 XP): Config Singleton + test muammosi
1. `config.js` modul-singleton yarating: `.env` ga o'xshash `config.json` dan o'qisin, `get(key)` metodi bo'lsin.
2. Unga bog'liq funksiya yozing (masalan, `getApiUrl()`) va Vitest bilan test qiling. Turli testlarda turli config kerak bo'lsa, qanday muammo chiqadi?
3. Muammoni DI bilan hal qiling: funksiya config'ni parametr sifatida qabul qilsin. `TAHLIL.md` da farqni tushuntiring.
