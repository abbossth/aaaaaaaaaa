# 9-dars challenge: "API detektivi" 🔎

**Vaqt:** 12 daqiqa | **Format:** juftlik

Quyidagi dict aslida real API javobi (qisqartirilgan). Uni Python fayliga nusxalang va savollarga **kod bilan** javob bering (qo'lda sanash taqiqlanadi!).

```python
javob = {
    "shahar": "Toshkent",
    "kunlar": [
        {"sana": "2026-10-01", "harorat": {"min": 12, "max": 24}, "holat": "quyoshli"},
        {"sana": "2026-10-02", "harorat": {"min": 14, "max": 26}, "holat": "bulutli"},
        {"sana": "2026-10-03", "harorat": {"min": 10, "max": 19}, "holat": "yomg'ir"},
        {"sana": "2026-10-04", "harorat": {"min": 9, "max": 17}, "holat": "yomg'ir"},
        {"sana": "2026-10-05", "harorat": {"min": 11, "max": 22}, "holat": "quyoshli"},
    ],
}
```

## Savollar
1. Eng issiq kun qaysi sana? (max bo'yicha)
2. Haftalik o'rtacha maksimal harorat?
3. Nechta kun yomg'irli?
4. Qanday ob-havo holatlari bo'lgan? (takrorsiz, set bilan)
5. Har bir kun uchun `"01-okt: 12°..24° ☀️"` formatida chiqaring (holatga qarab emoji: ☀️ ☁️ 🌧).

**XP:** 5 ta to'g'ri kod javob — 🥇 +20 · 🥈 +10 · 🥉 +5

Javob kaliti: 1) 2026-10-02 · 2) 21.6 · 3) 2 · 4) {'quyoshli', 'bulutli', "yomg'ir"}
