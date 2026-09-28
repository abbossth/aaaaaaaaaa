# 16-dars challenge: "API detektivi" 🔎

**Vaqt:** 15 daqiqa | **Format:** juftlik

Quyidagi JSON — real ob-havo API javobining soddalashtirilgan ko'rinishi. Uni `const javob = {...}` qilib yozing va savollarga **kod bilan** javob bering:

```js
const javob = {
  shahar: "Toshkent",
  kunlar: [
    { sana: "2026-10-01", harorat: { min: 12, max: 24 }, holat: "quyoshli" },
    { sana: "2026-10-02", harorat: { min: 14, max: 26 }, holat: "bulutli" },
    { sana: "2026-10-03", harorat: { min: 10, max: 19 }, holat: "yomg'ir" },
    { sana: "2026-10-04", harorat: { min: 9, max: 17 }, holat: "yomg'ir" },
    { sana: "2026-10-05", harorat: { min: 11, max: 22 }, holat: "quyoshli" },
  ],
};
```

1. Eng issiq kun sanasi?
2. O'rtacha maksimal harorat?
3. Nechta kun yomg'irli?
4. Qanday ob-havo holatlari bo'lgan (takrorsiz)?
5. Har bir kunni sahifada kartochka qilib chiqaring: `01-okt ☀️ 12°..24°`

**Javoblar:** 1) 2026-10-02 · 2) 21.6 · 3) 2 · 4) quyoshli, bulutli, yomg'ir
**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
