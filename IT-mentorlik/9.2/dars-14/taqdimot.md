# 14-dars slaydlari: OOP'ga kirish

## 1-slayd
🧟 **1 000 000 ta zombi. Qanday boshqaramiz?**

## 2-slayd — Klass va obyekt
🍪 **Klass** = pechenye qolipi (chizma)
🍪🍪🍪 **Obyekt** = qolipdan chiqqan pechenye (nusxa)
Bitta `Zombi` klassi → million `zombi` obyekti

## 3-slayd — Birinchi klass
```python
class Talaba:
    def __init__(self, ism, sinf):
        self.ism = ism          # atribut
        self.sinf = sinf
        self.baholar = []

aziz = Talaba("Aziz", "9.2")
malika = Talaba("Malika", "9.3")
print(aziz.ism)     # Aziz
```

## 4-slayd — self nima?
`self` = "men o'zim" (shu obyekt)
`aziz.ism` chaqirilganda `self` → `aziz`

## 5-slayd — Instance vs class atributi
```python
class Talaba:
    maktab = "42-maktab"       # CLASS atributi — hammaga umumiy
    soni = 0

    def __init__(self, ism):
        self.ism = ism         # INSTANCE atributi — har biriniki
        Talaba.soni += 1
```

## 6-slayd — dict vs klass
```python
# Oldin (dict)                  # Endi (klass)
t = {"ism": "Aziz"}             t = Talaba("Aziz")
t["ism"]                        t.ism
# xato yozsangiz: KeyError      # IDE avtomatik taklif qiladi ✨
```

## 7-slayd — OOP'ning 4 ustuni 🏛
🔒 Inkapsulyatsiya (16-dars) · 👨‍👦 Meros (17) · 🎭 Polimorfizm (17) · 🎨 Abstraksiya (18)
