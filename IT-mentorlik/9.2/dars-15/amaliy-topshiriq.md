# 15-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. 14-darsdagi `Kitob` klassiga `__str__` (`"O'tkan kunlar — A. Qodiriy"`) va `__repr__` qo'shing. `print(kitob)` va `print([kitob1, kitob2])` farqini ko'ring.
2. `Talaba` ga `@staticmethod baho_togrimi(baho)` qo'shing va `baho_qosh` ichida ishlating.

## 🟡 O'rta (+10 XP)
3. `Talaba.from_string("Aziz,9.2,15")` va `Talaba.from_dict({...})` classmethod'lari.
4. `Talaba` ga `__lt__` (o'rtacha baho bo'yicha) qo'shing va `sorted(talabalar)` bilan reyting chiqaring.
5. `Guruh` klassi: talabalar ro'yxatini saqlaydi. `__len__` (talabalar soni), `__contains__` (`"Aziz" in guruh`), `__iter__` (`for t in guruh:`).

## 🔴 Qiyin (+20 XP)
6. **Kasr (Fraction) klassi:** `Kasr(1, 2) + Kasr(1, 3) == Kasr(5, 6)`. `__add__`, `__sub__`, `__mul__`, `__eq__`, `__str__` (`"5/6"`). Kasr avtomatik qisqartirilsin (`math.gcd`). `Kasr(2, 4) == Kasr(1, 2)` → True.
