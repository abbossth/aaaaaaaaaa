# 7-dars slaydlari: Satrlar

## 1-slayd
🧹 `"  AZIZ@Mail.UZ "` → `"aziz@mail.uz"`

## 2-slayd — Indekslash
```
 S  a  l  o  m
 0  1  2  3  4
-5 -4 -3 -2 -1
```
`s[0]` → "S" · `s[-1]` → "m"

## 3-slayd — Kesish (slicing)
`s[start:stop:step]`
`s[1:4]` → "alo" · `s[:3]` → "Sal" · `s[::2]` → "Slm" · `s[::-1]` → "molaS"

## 4-slayd — Immutable (o'zgarmas)
```python
s = "Salom"
s[0] = "B"      # 💥 TypeError
s = "B" + s[1:] # ✅ yangi satr yaratiladi
```

## 5-slayd — Eng kerakli metodlar
| Metod | Natija |
|---|---|
| `.strip()` | chetdagi probellarni olib tashlaydi |
| `.lower()` / `.upper()` / `.title()` | harflar registri |
| `.replace(a, b)` | almashtirish |
| `.split(",")` | satr → ro'yxat |
| `"-".join(ro'yxat)` | ro'yxat → satr |
| `.find(x)` / `.count(x)` | qidirish / sanash |
| `.startswith()` / `.endswith()` | boshlanishi / tugashi |
| `.isdigit()` / `.isalpha()` | faqat raqammi / harfmi |

## 6-slayd — Back-end'da qo'llanilishi
Email normalizatsiya · telefonni tozalash · parolni tekshirish · slug yasash: `"Mening Birinchi Postim!"` → `"mening-birinchi-postim"`
