# 5-dars slaydlari: Sikllar va match/case

## 1-slayd
🎯 **1–100 oralig'idagi sonni 7 urinishda top!**

## 2-slayd — for + range
```python
for i in range(5):          # 0 1 2 3 4
for i in range(1, 6):       # 1 2 3 4 5
for i in range(10, 0, -2):  # 10 8 6 4 2
for harf in "Salom":        # S a l o m
```
❗ `range(1, 6)` — 6 kirmaydi!

## 3-slayd — while
```python
while shart:
    ...
while True:     # cheksiz, break bilan chiqiladi
    ...
```

## 4-slayd — break va continue
`break` — sikldan butunlay chiqish 🚪
`continue` — keyingi iteratsiyaga o'tish ⏭

## 5-slayd — for...else
```python
for n in sonlar:
    if n < 0:
        print("Manfiy topildi"); break
else:
    print("Manfiy yo'q")   # break bo'lmasa ishlaydi
```

## 6-slayd — match/case (Python 3.10+)
```python
match buyruq:
    case "start":
        print("Boshlandi")
    case "help" | "yordam":
        print("Yordam...")
    case _:
        print("Noma'lum buyruq")
```
