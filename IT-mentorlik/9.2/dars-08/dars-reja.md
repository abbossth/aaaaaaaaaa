# 8-dars. List va tuple

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Pythonda ma'lumotlar tuzilmalari: list, tuple"

## Maqsad
- Ro'yxat yaratadi, indekslaydi, kesadi va o'zgartiradi (mutable).
- Metodlarni qo'llaydi: `append, insert, extend, remove, pop, sort, reverse, index, count`, hamda `len, sum, min, max, sorted`.
- List comprehension bilan qisqa va o'qiladigan kod yozadi.
- Tuple'ning o'zgarmasligini, unpacking'ni (`a, b = b, a`) va qachon tuple ishlatilishini tushunadi.
- "Havola" (reference) muammosini biladi: `b = a` va `b = a.copy()`.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Uzum savatchangizda 5 ta mahsulot bor. Bittasini o'chirdingiz, bittasini qo'shdingiz, narx bo'yicha saraladingiz. Buning hammasi ro'yxat (list) bilan ishlash."* |
| 5–10 | **Takrorlash** | 7-dars testi |
| 10–28 | **Yangi mavzu** | List: yaratish, indeks, kesish, metodlar, `for`, `in`, `enumerate`. List comprehension. Tuple va unpacking. `copy` tuzog'i (jonli: `b = a; b.append(1); print(a)` 😱) |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Xarid savati" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
savat = ["non", "sut", "tuxum"]
savat.append("olma")
savat.insert(0, "choy")
savat.remove("sut")
oxirgi = savat.pop()
print(savat, len(savat))

narxlar = [12000, 5000, 30000, 8000]
print(sum(narxlar), max(narxlar), sorted(narxlar, reverse=True))

qimmat = [n for n in narxlar if n > 10000]
qqs_bilan = [n * 1.12 for n in narxlar]

for i, mahsulot in enumerate(savat, start=1):
    print(f"{i}. {mahsulot}")

nuqta = (41.31, 69.28)       # tuple — o'zgarmas
lat, lon = nuqta             # unpacking
a, b = 1, 2
a, b = b, a                  # almashtirish
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
