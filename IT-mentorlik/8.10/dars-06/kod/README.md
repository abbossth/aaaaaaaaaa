# 6-dars: psevdokod namunalari

## 1 dan 100 gacha yig'indi
```
Declare Integer i, summa
Assign summa = 0
For i = 1 to 100
    Assign summa = summa + i
End
Output "Yig'indi: " & summa
```

## Parol (3 urinish)
```
Declare String parol
Declare Integer urinish
Assign urinish = 0
Assign parol = ""
While parol != "dasturchi" and urinish < 3
    Output "Parolni kiriting:"
    Input parol
    Assign urinish = urinish + 1
End
If parol == "dasturchi"
    Output "Xush kelibsiz! Urinishlar: " & urinish
Else
    Output "Bloklandingiz!"
```
