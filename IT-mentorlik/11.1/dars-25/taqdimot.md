# 25-dars slaydlari: Sprint 1 🏃

## 1-slayd
**Sprint 1 · Maqsad: "yuruvchi skelet"**

## 2-slayd — Walking skeleton 💀🚶
❌ Avval butun front-end → keyin butun back-end → oxirida "ulaymiz"... va hech narsa ishlamaydi 😱
✅ Avval **bitta** funksiya **butun zanjir bo'ylab**: React tugma → fetch → Express → DB → javob → ekran
Keyin — qolgan funksiyalarni shu "skeletga" qo'shib borish

## 3-slayd — Monorepo tuzilmasi
```
startap/
├── web/            ← React (Vite)
│   └── src/
├── server/         ← Express API
│   └── src/
├── docs/           ← Lean Canvas, scrum.md, intervyular
├── .github/        ← PR shablon, keyinroq CI
└── README.md
```

## 4-slayd — Vite proxy (CORS'siz ishlab chiqish)
```js
// web/vite.config.js
export default { server: { proxy: { "/api": "http://localhost:3000" } } };
```
React'dan `fetch("/api/items")` → Vite uni Express'ga yo'naltiradi

## 5-slayd — Sprint qoidalari
- Har bir vazifa — alohida branch va PR
- DoD'ga amal qiling
- To'siq bo'lsa — **darhol** Scrum Master'ga
- Sprint Goal o'zgarmaydi!
