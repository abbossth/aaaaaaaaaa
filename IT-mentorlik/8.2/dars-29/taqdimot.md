# 29-dars slaydlari: Fayllar va xatolar 💾

## 1-slayd
**Dastur yopildi → ma'lumot yo'qoldi? Endi yo'q!**

## 2-slayd — try / except (JS: try/catch)
```python
try:
    yosh = int(input("Yosh: "))
except ValueError:
    print("Son kiriting!")
```

## 3-slayd — Fayllar
```python
with open("kundalik.txt", "a", encoding="utf-8") as f:
    f.write("Bugun Python o'rgandim!\n")

with open("kundalik.txt", encoding="utf-8") as f:
    print(f.read())
```
`"r"` o'qish · `"w"` yozish (**eskisini o'chiradi!**) · `"a"` oxiriga qo'shish

## 4-slayd — JSON (JS'dagi kabi!)
| JS | Python |
|---|---|
| `JSON.stringify(obj)` | `json.dumps(obj)` |
| `JSON.parse(str)` | `json.loads(str)` |
| `localStorage.setItem(...)` | `json.dump(obj, f)` (faylga) |
```python
import json
with open("lugat.json", "w", encoding="utf-8") as f:
    json.dump(lugat, f, ensure_ascii=False, indent=2)
```

## 5-slayd — Fayl yo'q bo'lsa?
```python
try:
    with open("lugat.json", encoding="utf-8") as f:
        lugat = json.load(f)
except FileNotFoundError:
    lugat = {}
```
