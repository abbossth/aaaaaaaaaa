# 3-dars. O'zgaruvchilar, ma'lumot turlari, input, f-string

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "O'zgaruvchilar va ma'lumotlarning sodda toifalari"

## Maqsad
- `int`, `float`, `str`, `bool` va `None` turlarini farqlaydi, `type()` bilan tekshiradi.
- Turlarni o'zgartirishni (`int()`, `float()`, `str()`) va uning xatolarini (`ValueError`) tushunadi.
- `input()` bilan ma'lumot oladi va f-string bilan chiroyli formatlaydi (`:.2f`, `:,`, `:>10`).
- O'zgaruvchilarni to'g'ri nomlaydi (snake_case, PEP 8).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Jonli: `input("Yoshingiz: ") + 1` → xato! *"Kompyuter '15' va 15 ni farqlaydi. Bugun nega shunday ekanini bilamiz. Bu xato real back-end'da har kuni uchraydi."* |
| 5–10 | **Takrorlash** | 2-dars testi |
| 10–28 | **Yangi mavzu** | O'zgaruvchi = "yorliqli quti". Turlar, `type()`, konvertatsiya, `input()` har doim `str`. f-string formatlash. Nomlash qoidalari |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–70 | **Challenge** | `challenge.md`: "Chek printer" |
| 70–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod (mentor ekranda yozadi)
```python
ism = "Aziz"            # str
yosh = 15               # int
boy = 1.68              # float
talabami = True         # bool
telefon = None          # hech narsa

print(type(yosh))       # <class 'int'>

yosh_matn = input("Yoshingiz: ")   # doim str!
yosh = int(yosh_matn)
print(f"Keyingi yil {yosh + 1} yoshda bo'lasiz")

narx = 1234567.891
print(f"{narx:,.2f} so'm")   # 1,234,567.89 so'm
print(f"|{ism:>10}|")        # |      Aziz|
```

## Baholash (XP)
- Amaliyot: +5/+10/+20 · Challenge: eng chiroyli va to'g'ri chek +30/+20/+10
