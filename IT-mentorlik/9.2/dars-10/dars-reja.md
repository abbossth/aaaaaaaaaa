# 10-dars. DRY prinsipi, funksiyalar, *args/**kwargs, lambda — "Kontaktlar kitobi" v2

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "DRY prinsipi. Pythonda funksiyalar"

## Maqsad
- DRY prinsipini tushunadi va takrorlanuvchi kodni funksiyalarga ajratadi.
- Funksiya e'lon qiladi va chaqiradi: pozitsion va nomlangan argumentlar, default qiymatlar, `return` (bir nechta qiymat ham).
- `*args`, `**kwargs`, `lambda` ni hamda `sorted/map/filter` bilan ishlatishni biladi.
- Scope'ni (lokal/global) tushunadi va docstring hamda type hint yozadi (`def f(x: int) -> str:`).
- "Kontaktlar kitobi" v1'ni funksiyalarga bo'lingan v2'ga refaktor qiladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | v1 kodida bir xil telefon tozalash kodi 3 joyda takrorlangan. *"Formatni o'zgartirish kerak bo'lsa, 3 joyni tuzatasiz, bittasini albatta unutasiz. DRY — Don't Repeat Yourself."* |
| 5–10 | **Takrorlash** | 9-dars testi + API detektivi javoblari |
| 10–28 | **Yangi mavzu** | `def`, parametr/argument, `return`, default, keyword args, `*args/**kwargs`, scope, lambda, type hints, docstring |
| 28–58 | **Amaliyot** | `amaliy-topshiriq.md`: Kontaktlar kitobi v2 |
| 58–72 | **Challenge** | `challenge.md`: "Funksiya fabrikasi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
def tozalash(tel: str) -> str | None:
    """Telefon raqamini 998XXXXXXXXX formatiga keltiradi. Noto'g'ri bo'lsa None."""
    raqamlar = "".join(c for c in tel if c.isdigit())
    if len(raqamlar) == 9:
        raqamlar = "998" + raqamlar
    return raqamlar if len(raqamlar) == 12 and raqamlar.startswith("998") else None

def salomlash(ism, til="uz"):
    return {"uz": f"Salom, {ism}!", "en": f"Hello, {ism}!"}.get(til, ism)

def statistika(*sonlar):
    return min(sonlar), max(sonlar), sum(sonlar) / len(sonlar)

def profil(**maydonlar):
    for k, v in maydonlar.items():
        print(f"{k}: {v}")

eng_kichik, eng_katta, ortacha = statistika(5, 3, 9, 1)
profil(ism="Aziz", sinf="9.2", shahar="Toshkent")
oquvchilar = [("Aziz", 87), ("Malika", 95)]
print(sorted(oquvchilar, key=lambda o: o[1], reverse=True))
```

## Baholash (XP)
- v2 refaktoring +5/+10/+20 · Challenge +30/+20/+10
