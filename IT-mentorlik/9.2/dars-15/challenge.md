# 15-dars challenge: "Pul klassi" 💰

**Vaqt:** 17 daqiqa | **Format:** juftlik

Real bank tizimlarida pul `float` bilan emas, maxsus klass bilan saqlanadi (`0.1 + 0.2` muammosini eslang!). Siz shunday klass yozing.

## Talablar
```python
a = Pul(15000)            # so'm (butun son, tiyinlarsiz)
b = Pul(5500)
print(a + b)              # 20 500 so'm
print(a - b)              # 9 500 so'm
print(a * 3)              # 45 000 so'm
print(a > b, a == Pul(15000))   # True True
print(sum([a, b, Pul(1000)], Pul(0)))   # 21 500 so'm
Pul(-100)                 # ValueError: Pul manfiy bo'lmaydi
a - Pul(20000)            # ValueError: Mablag' yetarli emas
```
- `__str__` minglik ajratgich sifatida **probel** ishlatsin
- `Pul.from_dollar(10, kurs=12800)` — classmethod

**Bonus (+10 XP):** `Pul(100000).taqsimla(3)` → `[Pul(33334), Pul(33333), Pul(33333)]` (qoldiq birinchisiga qo'shiladi, jami summa o'zgarmaydi!)

**XP:** barcha testlardan o'tgan birinchi 3 juftlik +30/+20/+10. Namuna: `kod/pul.py`
