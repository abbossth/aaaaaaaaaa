# 17-dars slaydlari: Meros va polimorfizm

## 1-slayd
⚔️🧙🏹 **Uch qahramon — bitta ota**

## 2-slayd — Meros
```python
class Qahramon:                       # ota
    def __init__(self, ism, hp):
        self.ism = ism
        self.hp = hp

class Jangchi(Qahramon):              # bola
    def __init__(self, ism):
        super().__init__(ism, hp=120)  # otaning konstruktori
        self.qalqon = 10
```

## 3-slayd — Override
```python
class Qahramon:
    def hujum(self): return 10

class Sehrgar(Qahramon):
    def hujum(self): return 25        # qayta yozildi
```

## 4-slayd — Polimorfizm 🎭
```python
jamoa = [Jangchi("Temur"), Sehrgar("Merlin"), Kamonchi("Robin")]
for q in jamoa:
    print(q.ism, q.hujum())   # har biri o'zicha!
```
"Bir xil buyruq — turli bajarilish"

## 5-slayd — isinstance
```python
isinstance(temur, Jangchi)    # True
isinstance(temur, Qahramon)   # True (u ham qahramon!)
issubclass(Jangchi, Qahramon) # True
```

## 6-slayd — Is-a vs Has-a
Jangchi **is a** Qahramon → **meros**
Qahramon **has a** Qurol → **kompozitsiya** (`self.qurol = Qilich()`)
❗ Qoida: "Kompozitsiyani merosdan afzal ko'ring"
