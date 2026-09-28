# 29-dars. Python: fayllar bilan ishlash, try/except — kundalik dasturi

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- Xatolarni `try / except / finally` bilan ushlaydi (JS'dagi `try/catch`).
- Aniq xato turlarini biladi: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`.
- `with open()` bilan fayl o'qiydi va yozadi (`r`, `w`, `a`, `encoding="utf-8"`).
- `json` moduli bilan ma'lumotni saqlaydi (JS'dagi `JSON.stringify/parse` + localStorage g'oyasi).
- "Shaxsiy kundalik" dasturini yaratadi: yozuvlar faylda saqlanadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Lug'at dasturiga (27-dars) 10 ta so'z qo'shish → dasturni yopish → qayta ochish → hammasi yo'qoldi 😱. *"JS'da localStorage bor edi. Python'da-chi? — Fayllar!"* |
| 5–10 | **Takrorlash** | 28-dars testi |
| 10–25 | **Yangi mavzu** | try/except. Fayllar. JSON (`dump`/`load`). JS ↔ Python |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md`: kundalik dasturi |
| 55–72 | **Challenge** | `challenge.md`: "Buzib ko'r" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge: har bir topilgan qulash +5
