# 4-dars. Operatorlar va ifodalar. Tarmoqlanuvchi algoritm (if/elif/else)

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Operatorlar va ifodalar. Tarmoqlanuvchi algoritm"

## Maqsad
- Arifmetik (`+ - * / // % **`), taqqoslash va mantiqiy (`and or not`) operatorlarni hamda ularning ustuvorligini biladi.
- `if / elif / else` va ichma-ich shartlarni yozadi, "truthy/falsy" qiymatlarni tushunadi.
- Ternar ifoda (`x if shart else y`) va zanjirli taqqoslashdan (`0 <= x <= 100`) foydalanadi.
- Real back-end mantiqini (login tekshiruvi, tarif hisoblash, validatsiya) shartlar bilan yozadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Savol: *"Yandex Go narxni qanday hisoblaydi?"* Masofa, vaqt, tarif, tungi koeffitsiyent, "yuqori talab"... *"Bularning hammasi if'lar. Bugun o'z taksi tarif dvigatelimizni yozamiz."* |
| 5–10 | **Takrorlash** | 3-dars testi + uyga vazifa tekshiruvi (BMI) |
| 10–25 | **Yangi mavzu** | Operatorlar jadvali, ustuvorlik. `if/elif/else`, ichma-ich if. Truthy/falsy (`0, "", [], None`). Ternar ifoda. Zanjirli taqqoslash |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Taksi tarif dvigateli" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
login = input("Login: ")
parol = input("Parol: ")

if not login or not parol:
    print("Maydonlar bo'sh bo'lmasin!")
elif login == "admin" and parol == "12345":
    print("Xush kelibsiz, admin!")
elif login == "admin":
    print("Parol noto'g'ri")
else:
    print("Bunday foydalanuvchi yo'q")

yosh = 15
holat = "voyaga yetgan" if yosh >= 18 else "voyaga yetmagan"
print(0 <= yosh <= 120)   # zanjirli taqqoslash
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
