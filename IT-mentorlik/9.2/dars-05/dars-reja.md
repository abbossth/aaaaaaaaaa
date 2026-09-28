# 5-dars. Takrorlanuvchi algoritm: for, while, range, break/continue. match/case

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Takrorlanuvchi algoritm, takrorlanish operatorlari"

## Maqsad
- `for` va `range(start, stop, step)`, `while`, `break`, `continue`, `for...else` konstruksiyalarini qo'llaydi.
- Hisoblagich, yig'uvchi va "flag" o'zgaruvchilaridan foydalanadi.
- `match/case` (Python 3.10+) bilan menyu va komandalarni qayta ishlaydi.
- Terminal menyuli interaktiv dastur yozadi (keyinchalik bot uchun asos bo'ladi).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Jonli: "Son topish" o'yini, kompyuter 1–100 oralig'ida son o'yladi. Sinf taxmin qiladi, kompyuter "katta/kichik" deydi. 7 urinishda topiladi. *"Bu o'yinni 15 qatorda yozamiz. Nega 7 urinish yetarli? Bu binar qidiruv, algoritmlarning qiroli."* |
| 5–10 | **Takrorlash** | 4-dars testi |
| 10–25 | **Yangi mavzu** | `for`/`range`, `while`, `break`/`continue`, `for...else`, `match/case` |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Bankomat simulyatori" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod: son topish
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
- Amaliyot +5/+10/+20 · Bankomat +30/+20/+10
