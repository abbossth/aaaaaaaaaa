# 18-dars slaydlari: Abstraksiya

## 1-slayd
🚗 **Rul, gaz, tormoz — dvigatel ichini bilmasdan haydaysiz**

## 2-slayd — Abstraksiya
Murakkablikni yashirish → faqat kerakli "tugmalar"ni ko'rsatish
Do'kon: `provayder.tolov(summa)` — Click'mi, Payme'mi, farqi yo'q

## 3-slayd — abc moduli
```python
from abc import ABC, abstractmethod

class TolovProvayderi(ABC):
    @abstractmethod
    def tolov(self, summa: int) -> str: ...

    @abstractmethod
    def qaytarish(self, tranzaksiya_id: str) -> bool: ...
```

## 4-slayd — Shartnoma
```python
TolovProvayderi()   # 💥 TypeError: Can't instantiate abstract class

class Click(TolovProvayderi):
    def tolov(self, summa): ...
    # qaytarish() yozilmadi →
Click()             # 💥 TypeError!
```
Abstrakt klass — **barcha bolalar bajarishi shart bo'lgan shartnoma**

## 5-slayd — Duck typing 🦆
*"Agar u o'rdakdek yursa va o'rdakdek g'aqillasa — demak, o'rdak."*
Python'da `tolov()` metodi bo'lsa kifoya. ABC esa bu qoidani **majburiy** qiladi

## 6-slayd — OOP'ning 4 ustuni 🏛
🔒 **Inkapsulyatsiya:** holatni himoya qilish (16)
👨‍👦 **Meros:** kodni qayta ishlatish (17)
🎭 **Polimorfizm:** bir interfeys — ko'p bajarilish (17)
🎨 **Abstraksiya:** murakkablikni yashirish, shartnoma (18)
