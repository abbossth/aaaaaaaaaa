# 11-dars. try/except/finally, raise, fayllar (with open), JSON — "Kontaktlar kitobi" v3

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Istisnoli holatlarni dasturlash (try/except). Fayllar bilan ishlash"

## Maqsad
- Istisno (exception) nima ekanini biladi va `try/except/else/finally` bilan xatolarni ushlaydi.
- Aniq xato turlarini ushlaydi (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`) va nega `except:` (hammasini) yomon ekanini tushunadi.
- `raise` bilan o'z xatosini chiqaradi va o'z xato klassini yaratadi.
- `with open()` bilan fayl o'qiydi va yozadi (`r`, `w`, `a` rejimlari, `encoding="utf-8"`).
- `json.dump` / `json.load` bilan ma'lumotni saqlaydi. **Kontaktlar kitobi v3** endi dastur yopilsa ham ma'lumotni yo'qotmaydi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | v2'ni ishga tushirish → 3 ta kontakt qo'shish → dasturni yopish → qayta ochish → hammasi yo'qoldi 😱. Yoshga "o'n besh" deb yozish → dastur qulaydi. *"Real ilova hech qachon bunday qilmasligi kerak."* |
| 5–10 | **Takrorlash** | 10-dars testi |
| 10–28 | **Yangi mavzu** | try/except/else/finally, xato turlari, raise, custom exception. Fayllar: open, with, rejimlar, encoding. JSON |
| 28–58 | **Amaliyot** | `amaliy-topshiriq.md`: Kontaktlar v3 |
| 58–72 | **Challenge** | `challenge.md`: "Buzib ko'r" (hacker-tester) |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
import json
from pathlib import Path

FAYL = Path("kontaktlar.json")

def yuklash() -> dict:
    try:
        with open(FAYL, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("⚠️ Fayl buzilgan, bo'sh ro'yxat bilan boshlaymiz")
        return {}

def saqlash(data: dict) -> None:
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def son_sora(xabar: str) -> int:
    while True:
        try:
            return int(input(xabar))
        except ValueError:
            print("❌ Iltimos, son kiriting")
```

## Baholash (XP)
- v3 +5/+10/+20 · "Buzib ko'r": har bir topilgan qulash +5
