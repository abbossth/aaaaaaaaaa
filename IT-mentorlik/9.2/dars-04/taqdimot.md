# 4-dars slaydlari: Operatorlar va shartlar

## 1-slayd
🚕 **Yandex Go narxni qanday hisoblaydi?** → `if` lar!

## 2-slayd — Arifmetik operatorlar
`+` `-` `*` `/` (doim float) · `//` butun bo'lish · `%` qoldiq · `**` daraja
`7 / 2 = 3.5` · `7 // 2 = 3` · `7 % 2 = 1` · `2 ** 10 = 1024`

## 3-slayd — Taqqoslash va mantiq
`==` `!=` `>` `<` `>=` `<=`
`and` (ikkalasi) · `or` (bittasi) · `not` (teskari)
Ustuvorlik: `**` → `* / // %` → `+ -` → taqqoslash → `not` → `and` → `or`

## 4-slayd — if / elif / else
```python
if ball >= 86:
    baho = 5
elif ball >= 71:
    baho = 4
else:
    baho = 3
```
❗ Chekinish (indent) — 4 ta probel

## 5-slayd — Truthy / Falsy
Falsy: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `None`
Qolgan hammasi — Truthy
```python
if ism:        # ism bo'sh bo'lmasa
```

## 6-slayd — Qisqa yozuvlar
```python
holat = "juft" if n % 2 == 0 else "toq"     # ternar
if 0 <= ball <= 100:                        # zanjir
```
