# 11-dars slaydlari: Xatolar va fayllar

## 1-slayd
💥 **Dastur qulamasligi va xotirani yo'qotmasligi kerak**

## 2-slayd — try / except
```python
try:
    yosh = int(input("Yosh: "))
except ValueError:
    print("Son kiriting!")
else:
    print("Rahmat!")          # xato bo'lmasa
finally:
    print("Har doim ishlaydi") # fayl/ulanishni yopish
```

## 3-slayd — Xato turlari
`ValueError` `int("abc")` · `ZeroDivisionError` `1/0` · `KeyError` `d["yo'q"]`
`IndexError` `l[99]` · `FileNotFoundError` · `TypeError` `"1" + 1`

## 4-slayd — ❌ except: hammasini ushlash
```python
try: ...
except:        # ❌ xatolarni "yutib yuboradi", debug qilib bo'lmaydi
    pass
```
✅ Aniq turini ushlang: `except ValueError as e:`

## 5-slayd — raise
```python
def yosh_tekshir(yosh):
    if not 0 < yosh < 120:
        raise ValueError(f"Noto'g'ri yosh: {yosh}")

class BalansYetarliEmas(Exception):
    pass
```

## 6-slayd — Fayllar
```python
with open("fayl.txt", "w", encoding="utf-8") as f:
    f.write("Salom\n")
with open("fayl.txt", encoding="utf-8") as f:
    matn = f.read()
```
`r` o'qish · `w` yozish (ustiga!) · `a` oxiriga qo'shish
`with` — faylni avtomatik yopadi ✅

## 7-slayd — JSON
```python
import json
json.dump(data, f, ensure_ascii=False, indent=2)   # dict → fayl
data = json.load(f)                                # fayl → dict
```
`ensure_ascii=False` → o'zbekcha harflar to'g'ri saqlanadi
