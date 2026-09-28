# 27-dars slaydlari: Python tuzilmalari 📦

## 1-slayd
**4 ta "quti": list, tuple, set, dict**

## 2-slayd — Jadval
| Python | JS | Xususiyat | Misol |
|---|---|---|---|
| `list` | array | tartibli, o'zgaradi | `[1, 2, 3]` |
| `tuple` | — | tartibli, **o'zgarmaydi** | `(41.3, 69.2)` |
| `set` | Set | **takrorsiz** | `{1, 2, 3}` |
| `dict` | object | kalit: qiymat | `{"ism": "Aziz"}` |

## 3-slayd — list
```python
mevalar = ["olma", "nok"]
mevalar.append("uzum")      # JS: push
mevalar.pop()               # JS: pop
len(mevalar)                # JS: .length
sorted(sonlar)              # yangi ro'yxat
```

## 4-slayd — List comprehension ✨ (JS: map/filter)
```python
kvadratlar = [x ** 2 for x in range(1, 6)]            # map
juftlar = [x for x in sonlar if x % 2 == 0]           # filter
nomlar = [m["nom"] for m in mahsulotlar if m["narx"] < 1_000_000]   # filter + map
```

## 5-slayd — dict = JSON!
```python
talaba = {"ism": "Aziz", "yosh": 14}
talaba["sinf"] = "8.2"               # qo'shish
talaba.get("tel", "yo'q")            # xavfsiz o'qish
for kalit, qiymat in talaba.items():
    print(kalit, qiymat)
```

## 6-slayd — set
```python
set([1, 1, 2, 3, 3])      # {1, 2, 3}
{"a", "b"} & {"b", "c"}   # {"b"} — kesishma
```
