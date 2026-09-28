# 28-dars slaydlari: Python funksiyalari

## 1-slayd
🔐 **"123456" — 1 soniyada buziladi**

## 2-slayd — JS ↔ Python
```js
function salom(ism = "mehmon") { return `Salom, ${ism}!`; }
const kvadrat = (x) => x * x;
```
```python
def salom(ism="mehmon"):
    return f"Salom, {ism}!"

kvadrat = lambda x: x * x
```

## 3-slayd — Bir nechta qiymat qaytarish
```python
def min_max(sonlar):
    return min(sonlar), max(sonlar)

kichik, katta = min_max([3, 9, 1])
```

## 4-slayd — Modullar
```python
import random
import string
from datetime import date

random.choice(string.ascii_letters)
date.today()
```
O'z modulingiz: `utils.py` → `from utils import parol_yarat`

## 5-slayd — lambda + sorted
```python
oquvchilar = [("Aziz", 87), ("Malika", 95)]
sorted(oquvchilar, key=lambda o: o[1], reverse=True)
```
(JS: `.sort((a, b) => b[1] - a[1])`)
