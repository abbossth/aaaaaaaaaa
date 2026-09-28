# 30-dars slaydlari: OOP 🍪

## 1-slayd
🧟 **1 000 000 zombi — bitta klass**

## 2-slayd — Klass va obyekt
🍪 **Klass** = pechenye qolipi (chizma)
🍪🍪🍪 **Obyekt** = qolipdan chiqqan pechenye

## 3-slayd — Birinchi klass
```python
class BankHisobi:
    def __init__(self, egasi, balans=0):   # konstruktor
        self.egasi = egasi                 # atribut
        self.balans = balans

    def qoyish(self, summa):               # metod
        self.balans += summa

    def __str__(self):
        return f"{self.egasi}: {self.balans:,} so'm"

aziz = BankHisobi("Aziz", 50000)
aziz.qoyish(20000)
print(aziz)          # Aziz: 70,000 so'm
```

## 4-slayd — self = "men o'zim"
`aziz.qoyish(20000)` → metod ichida `self` = `aziz`

## 5-slayd — JS ↔ Python
```js
class BankHisobi {
  constructor(egasi, balans = 0) { this.egasi = egasi; this.balans = balans; }
  qoyish(summa) { this.balans += summa; }
}
```
`constructor` → `__init__` · `this` → `self`

## 6-slayd — Nega muhim?
Django'da har bir jadval — **klass** (45-dars):
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
```
