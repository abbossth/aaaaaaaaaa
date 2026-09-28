# 15-dars. Metodlar: instance, class, static va maxsus (dunder) metodlar

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Metodlar: instance, static, class va maxsus metodlar"

## Maqsad
- Instance metod (`self`), class metod (`@classmethod`, `cls`) va static metod (`@staticmethod`) farqini biladi.
- `@classmethod` ni "muqobil konstruktor" (`from_dict`, `from_string`) sifatida ishlatadi.
- Maxsus metodlarni (`__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`) yozadi va obyektni Python'ning "o'z" turlari kabi ishlatadi.
- `Pul` yoki `Vektor` kabi "aqlli" klass yaratadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | `print(aziz)` → `<__main__.Talaba object at 0x7f...>` 🤢. *"Nega `print([1,2])` chiroyli chiqadi, bizning obyekt esa yo'q? Nega `len("salom")` ishlaydi? Bugun obyektlarimizga 'sehr' qo'shamiz."* |
| 5–10 | **Takrorlash** | 14-dars testi |
| 10–28 | **Yangi mavzu** | 3 turdagi metod (jadval). Dunder metodlar: Python sizning obyektingiz bilan qanday "gaplashadi" |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Pul klassi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
