# 3-dars slaydlari: O'zgaruvchilar va turlar

## 1-slayd
`"15" + 1` → 💥 TypeError. Nega?

## 2-slayd — O'zgaruvchi = yorliqli quti 📦
```python
ism = "Aziz"
```
`ism` — yorliq, `"Aziz"` — qutidagi narsa, `=` — "qutiga solish"

## 3-slayd — Asosiy turlar
| Tur | Misol | Nima |
|---|---|---|
| `int` | `15`, `-3`, `0` | Butun son |
| `float` | `3.14`, `1.68` | Kasr son |
| `str` | `"Salom"`, `'15'` | Matn |
| `bool` | `True`, `False` | Rost/yolg'on |
| `NoneType` | `None` | Hech narsa |

## 4-slayd — input() har doim str qaytaradi!
```python
yosh = input("Yosh: ")   # "15"
yosh = int(yosh)         # 15
```
`int("salom")` → 💥 ValueError

## 5-slayd — f-string sehrlari ✨
```python
f"{narx:.2f}"    # 2 xonali kasr
f"{narx:,}"      # 1,234,567
f"{ism:>10}"     # o'ngga tekislash
f"{ism:^10}"     # markazga
f"{0.853:.0%}"   # 85%
```

## 6-slayd — Nomlash qoidalari (PEP 8)
✅ `talaba_ismi`, `umumiy_narx`, `MAX_BALL`
❌ `TalabaIsmi`, `a1`, `2ism`, `class`, `umumiy narx`
