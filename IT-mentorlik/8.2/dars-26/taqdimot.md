# 26-dars slaydlari: Shartlar va sikllar 🐍

## 1-slayd
**JS'dan Python'ga: shartlar va sikllar**

## 2-slayd — if / elif / else
```python
if ball >= 86:
    print("A'lo")
elif ball >= 71:          # JS: else if
    print("Yaxshi")
else:
    print("Harakat qil!")
```
`and` (JS: `&&`) · `or` (`||`) · `not` (`!`)

## 3-slayd — for va range
```python
for i in range(5):          # 0 1 2 3 4
for i in range(1, 11):      # 1 ... 10  (11 KIRMAYDI!)
for i in range(10, 0, -2):  # 10 8 6 4 2
for harf in "Salom":        # S a l o m
```

## 4-slayd — while, break, continue
```python
while True:
    javob = input("Davom etamizmi? ")
    if javob == "yo'q":
        break
```

## 5-slayd — random moduli
```python
import random
random.randint(1, 6)                  # 🎲 1..6
random.choice(["tosh", "qaychi", "qog'oz"])
```
