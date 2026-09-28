# 10-dars slaydlari: Funksiyalar

## 1-slayd
♻️ **DRY — Don't Repeat Yourself**

## 2-slayd — Funksiya = mini-dastur
```python
def kvadrat(x):
    return x ** 2

kvadrat(5)   # 25
```
`def` — e'lon · `x` — parametr · `5` — argument · `return` — natija

## 3-slayd — Argumentlar
```python
def salom(ism, til="uz"):       # default qiymat
    ...
salom("Aziz")                   # pozitsion
salom(til="en", ism="Aziz")     # nomlangan (keyword)
```

## 4-slayd — Bir nechta qiymat qaytarish
```python
def min_max(l):
    return min(l), max(l)       # tuple
a, b = min_max([3, 1, 9])
```

## 5-slayd — *args va **kwargs
```python
def yigindi(*sonlar): return sum(sonlar)       # tuple
def profil(**maydonlar): print(maydonlar)       # dict
yigindi(1, 2, 3, 4)
profil(ism="Aziz", yosh=15)
```

## 6-slayd — Lambda
```python
kvadrat = lambda x: x ** 2
sorted(oquvchilar, key=lambda o: o["ball"])
list(filter(lambda x: x % 2 == 0, sonlar))
list(map(lambda x: x * 1.12, narxlar))
```

## 7-slayd — Scope
Funksiya ichidagi o'zgaruvchi — **lokal**, tashqarida ko'rinmaydi.
`global` — kamdan-kam va ehtiyotkorlik bilan!

## 8-slayd — Professional funksiya
```python
def narx_hisobla(narx: float, soni: int = 1, qqs: float = 0.12) -> float:
    """Mahsulotning QQS bilan umumiy narxini qaytaradi."""
    return narx * soni * (1 + qqs)
```
