# 26-dars. Python: shartlar va sikllar — "Son topish" o'yini

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- `if / elif / else`, taqqoslash va mantiqiy operatorlarni (`and, or, not`) Python'da yozadi.
- `for` + `range()`, `while`, `break`, `continue` ni qo'llaydi.
- JS'dagi sikllar bilan farqini biladi (`range(1, 11)` — 11 kirmaydi!).
- `random` moduli bilan "Son topish" o'yinini yaratadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 13-darsdagi JS "Son topish" o'yinini eslash: *"Bugun uni Python'da 15 qatorda yozamiz va solishtiramiz."* |
| 5–10 | **Takrorlash** | 25-dars testi |
| 10–25 | **Yangi mavzu** | if/elif/else (JS'dagi `else if` → `elif`). for/range, while, break/continue. `random.randint` |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Son topish" + "Tosh-qaychi-qog'oz" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
import random

son = random.randint(1, 100)
urinish = 0
while True:
    taxmin = int(input("Taxmin: "))
    urinish += 1
    if taxmin < son:
        print("Kattaroq ⬆️")
    elif taxmin > son:
        print("Kichikroq ⬇️")
    else:
        print(f"Topdingiz! {urinish} urinishda 🎉")
        break
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
