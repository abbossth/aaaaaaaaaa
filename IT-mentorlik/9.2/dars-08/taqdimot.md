# 8-dars slaydlari: List va Tuple

## 1-slayd
🛒 **Savat = ro'yxat (list)**

## 2-slayd — List
```python
mevalar = ["olma", "nok", "uzum"]
mevalar[0]      # "olma"
mevalar[-1]     # "uzum"
mevalar[1] = "anor"   # ✅ o'zgartirish mumkin (mutable)
```

## 3-slayd — Metodlar
| Qo'shish | O'chirish | Tartib |
|---|---|---|
| `append(x)` oxiriga | `remove(x)` qiymat bo'yicha | `sort()` joyida |
| `insert(i, x)` joyga | `pop()` / `pop(i)` indeks bo'yicha | `reverse()` |
| `extend(list)` bir nechta | `clear()` hammasi | `sorted(l)` yangi ro'yxat |

## 4-slayd — List comprehension ✨
```python
kvadratlar = [x ** 2 for x in range(1, 6)]     # [1, 4, 9, 16, 25]
juftlar = [x for x in sonlar if x % 2 == 0]
```

## 5-slayd — Tuple
```python
rang = (255, 0, 0)          # o'zgarmas
rang[0] = 100               # 💥 TypeError
x, y = (10, 20)             # unpacking
```
Qachon: koordinatalar, RGB, funksiyadan bir nechta qiymat qaytarish, dict kaliti

## 6-slayd — ⚠️ Havola tuzog'i
```python
a = [1, 2, 3]
b = a           # b — o'sha ro'yxatning ikkinchi nomi!
b.append(4)
print(a)        # [1, 2, 3, 4] 😱
b = a.copy()    # ✅ haqiqiy nusxa
```
