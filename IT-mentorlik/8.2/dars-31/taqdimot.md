# 31-dars slaydlari: Meros va polimorfizm ⚔️

## 1-slayd
⚡ **Pikachu vs 🔥 Charmander** — ikkalasi ham Pokemon, lekin har xil!

## 2-slayd — Meros = "otadan bolaga"
```python
class Pokemon:                       # ota (asosiy) klass
    def __init__(self, ism, hp, kuch):
        self.ism = ism
        self._hp = hp                # _ = "tegmang" (himoyalangan)
        self.kuch = kuch

    def hujum(self, raqib):
        raqib.zarar_ol(self.kuch)
        return f"{self.ism} oddiy hujum qildi!"

class Olov(Pokemon):                 # bola klass
    pass                             # hamma narsani otadan oladi
```

## 3-slayd — super() va override
```python
class Olov(Pokemon):
    def __init__(self, ism, hp, kuch):
        super().__init__(ism, hp, kuch)   # otaning __init__'i
        self.tur = "🔥"

    def hujum(self, raqib):               # QAYTA YOZISH (override)
        raqib.zarar_ol(self.kuch * 1.5)
        return f"{self.ism} olov purkadi! 🔥"
```

## 4-slayd — Polimorfizm = "bitta buyruq, har xil natija"
```python
jamoa = [Olov("Charmander", 100, 12), Suv("Squirtle", 110, 10), Elektr("Pikachu", 90, 14)]
for p in jamoa:
    print(p.hujum(dushman))   # har biri o'zicha hujum qiladi
```

## 5-slayd — Inkapsulyatsiya: @property
```python
    @property
    def hp(self):
        return self._hp

    def zarar_ol(self, miqdor):
        self._hp = max(0, self._hp - int(miqdor))   # hech qachon manfiy emas
```
`p.hp = -500` ❌ — ruxsat yo'q (setter yo'q)

## 6-slayd — OOP 4 ustuni
| Ustun | Ma'nosi |
|---|---|
| Inkapsulyatsiya | Ichki ma'lumotni himoyalash |
| Meros | Otadan xususiyat olish |
| Polimorfizm | Bitta metod — har xil xatti-harakat |
| Abstraksiya | Keraksiz tafsilotni yashirish |
