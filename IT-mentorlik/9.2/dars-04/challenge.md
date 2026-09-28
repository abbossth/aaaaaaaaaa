# 4-dars challenge: "Taksi tarif dvigateli" 🚕

**Vaqt:** 17 daqiqa | **Format:** juftlik

Taksi narxini hisoblovchi dastur yozing. Kiritiladi: **masofa (km)**, **vaqt (soat, 0–23)**, **tarif** ("ekonom", "komfort", "biznes"), **yomg'ir yog'yaptimi** (ha/yo'q).

## Qoidalar
| Tarif | Boshlang'ich | 1 km |
|---|---|---|
| ekonom | 7 000 | 2 000 |
| komfort | 10 000 | 2 800 |
| biznes | 20 000 | 4 500 |

- Tungi vaqt (22:00–06:00): narx × 1.2
- Yomg'ir: narx × 1.3
- Minimal narx: tarifning boshlang'ich narxidan kam bo'lmasin
- 50 km dan uzoq masofa: 10% chegirma
- Noto'g'ri tarif yoki soat kiritilsa: tushunarli xato xabari

## Mentor test qiladi
| Kirish | Kutilgan natija |
|---|---|
| 10 km, 14, ekonom, yo'q | 27 000 |
| 10 km, 23, komfort, ha | (10000+28000)×1.2×1.3 = 59 280 |
| 60 km, 12, ekonom, yo'q | (7000+120000)×0.9 = 114 300 |
| 5 km, 25, ekonom, yo'q | Xato: soat noto'g'ri |

**XP:** hamma testdan o'tgan birinchi 3 juftlik: +30/+20/+10. Barcha testdan o'tganlarga +10.
