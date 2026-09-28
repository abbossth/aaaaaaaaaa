# 15-dars slaydlari: Metodlar va dunder sehrlari ✨

## 1-slayd
`<__main__.Talaba object at 0x7f3a...>` 🤢 → `Talaba(Aziz, 9.2)` 😍

## 2-slayd — 3 turdagi metod
| Tur | Birinchi parametr | Nima uchun |
|---|---|---|
| Instance | `self` | Obyekt ma'lumoti bilan ishlash |
| `@classmethod` | `cls` | Muqobil konstruktor, klass bilan ishlash |
| `@staticmethod` | yo'q | Klassga mantiqan tegishli yordamchi funksiya |

## 3-slayd — classmethod: muqobil konstruktor
```python
class Talaba:
    @classmethod
    def from_string(cls, satr):          # "Aziz,9.2,15"
        ism, sinf, yosh = satr.split(",")
        return cls(ism, sinf, int(yosh))

t = Talaba.from_string("Aziz,9.2,15")
```

## 4-slayd — staticmethod
```python
class Talaba:
    @staticmethod
    def baho_togrimi(baho):
        return 2 <= baho <= 5
```

## 5-slayd — Dunder (double underscore) metodlar
| Metod | Qachon chaqiriladi |
|---|---|
| `__str__` | `print(obj)`, `str(obj)` — foydalanuvchi uchun |
| `__repr__` | Console, debug — dasturchi uchun |
| `__len__` | `len(obj)` |
| `__eq__` | `a == b` |
| `__lt__` | `a < b`, `sorted()` |
| `__add__` | `a + b` |

## 6-slayd — Misol
```python
class Pul:
    def __init__(self, summa): self.summa = summa
    def __add__(self, other): return Pul(self.summa + other.summa)
    def __str__(self): return f"{self.summa:,} so'm"

print(Pul(5000) + Pul(12000))   # 17,000 so'm
```
