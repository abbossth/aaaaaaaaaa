# 9-dars slaydlari: Set va Dict

## 1-slayd
`{"login": "torvalds", "followers": 250000}` — bu JSON... yoki Python dict? **Ikkalasi ham!**

## 2-slayd — Set
```python
s = {1, 2, 2, 3}      # {1, 2, 3} — takror yo'q
unikal = set(royxat)
"x" in s              # juda tez!
```

## 3-slayd — Set amallari
```python
futbol = {"Aziz", "Bobur", "Sardor"}
shaxmat = {"Aziz", "Malika"}
futbol | shaxmat   # birlashma: hammasi
futbol & shaxmat   # kesishma: {"Aziz"}
futbol - shaxmat   # ayirma: {"Bobur", "Sardor"}
futbol ^ shaxmat   # simmetrik ayirma
```

## 4-slayd — Dictionary
```python
talaba = {"ism": "Aziz", "yosh": 15, "sinf": "9.2"}
talaba["ism"]                 # "Aziz"
talaba.get("tel", "yo'q")     # "yo'q" (xatosiz)
talaba["tel"] = "+998..."     # qo'shish
del talaba["yosh"]            # o'chirish
```

## 5-slayd — Aylanib chiqish
```python
for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")
```

## 6-slayd — Ichma-ich dict = JSON
```python
kontaktlar = {
    "Aziz": {"tel": "998901234567", "email": "aziz@mail.uz", "teglar": ["do'st"]},
    "Malika": {"tel": "998907654321", "email": None, "teglar": ["sinfdosh"]},
}
kontaktlar["Aziz"]["tel"]
```

## 7-slayd — Dict comprehension
```python
harflar = {h: matn.count(h) for h in set(matn)}
kvadratlar = {x: x ** 2 for x in range(1, 6)}
```
