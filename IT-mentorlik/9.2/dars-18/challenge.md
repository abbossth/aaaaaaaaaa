# 18-dars challenge: "Shartnomani buz" 📜

**Vaqt:** 14 daqiqa | **Format:** jamoalar

Mentor abstrakt klass beradi:
```python
class OyinPersonaji(ABC):
    @abstractmethod
    def harakat(self, yonalish: str) -> None: ...
    @abstractmethod
    def hujum(self) -> int: ...
    @abstractmethod
    def malumot(self) -> str: ...
```

## 1-raund (7 daqiqa)
Jamoalar 3 xil personaj yozadi. Mentor har birini tekshiruvchi skript bilan sinaydi:
```python
for p in personajlar:
    p.harakat("oldinga"); assert isinstance(p.hujum(), int); print(p.malumot())
```

## 2-raund (7 daqiqa)
Mentor abstrakt klassga **yangi** abstrakt metod qo'shadi: `sakrash()`. Nima bo'ldi? Barcha personajlar "buzildi" — ularni tezda tuzating!

**Xulosa:** abstrakt klassga metod qo'shish = barcha bolalarni o'zgartirish. Shuning uchun interfeyslar ehtiyotkorlik bilan loyihalanadi (SOLID'dagi ISP).

**XP:** birinchi tuzatgan jamoalar 🥇 +20 · 🥈 +10 · 🥉 +5
