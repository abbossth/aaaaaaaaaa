# 9-dars. Set va dictionary — "Kontaktlar kitobi" v1

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Pythonda ma'lumotlar tuzilmalari: set va dictionary"

## Maqsad
- Set'ning xususiyatlarini (takrorlanmas, tartibsiz) va amallarini (`|`, `&`, `-`, `^`) biladi.
- Dictionary (kalit: qiymat) yaratadi, o'qiydi (`d[k]`, `d.get(k, default)`), o'zgartiradi va o'chiradi.
- `keys()`, `values()`, `items()` bilan aylanib chiqadi. Ichma-ich dict (JSON'ga o'xshash tuzilma) bilan ishlaydi.
- List, tuple, set va dict'dan qaysi birini qachon tanlashni biladi.
- Yil davomidagi mini loyiha — **"Kontaktlar kitobi" v1** ni boshlaydi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Brauzerda `https://api.github.com/users/torvalds`: JSON = Python dict! *"Internetdagi barcha API'lar dict ko'rinishida gaplashadi. Dict'ni bilsangiz, API'ni bilasiz."* |
| 5–10 | **Takrorlash** | 8-dars testi |
| 10–18 | **Set** | Takrorlarni olib tashlash, `in` tezligi, to'plam amallari (Venn diagrammasi: "futbol va shaxmat o'ynaydiganlar") |
| 18–30 | **Dict** | Yaratish, o'qish, `get`, qo'shish, o'chirish, `items()`, ichma-ich dict, dict comprehension. Harf sanagich (7-dars uyga vazifasi) 1 qatorda |
| 30–60 | **Amaliyot** | `amaliy-topshiriq.md`: Kontaktlar kitobi v1 |
| 60–72 | **Challenge** | `challenge.md`: "API detektivi" |
| 72–80 | **Yakun** | "Qaysi tuzilmani qachon?" jadvali, XP, uyga vazifa |

## Qaysi tuzilmani qachon? (doskaga)
| Tuzilma | Qachon |
|---|---|
| `list` | Tartib muhim, takror bo'lishi mumkin, o'zgaradi |
| `tuple` | O'zgarmas yozuv (koordinata, RGB) |
| `set` | Takrorlanmas elementlar, tez tekshirish (`in`) |
| `dict` | Kalit bo'yicha qidirish (telefon kitobi, JSON) |

## Baholash (XP)
- Kontaktlar kitobi +5/+10/+20 · Challenge +20/+10/+5
