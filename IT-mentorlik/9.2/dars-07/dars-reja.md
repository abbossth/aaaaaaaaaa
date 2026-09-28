# 7-dars. Satrlar (string) va ularning metodlari

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Pythonda ma'lumotlar tuzilmalari: string"

## Maqsad
- Satr indekslash (`s[0]`, `s[-1]`) va kesish (`s[1:4]`, `s[::-1]`) amallarini bajaradi.
- Satrlarning o'zgarmasligini (immutable) tushunadi.
- Asosiy metodlarni qo'llaydi: `upper/lower/title/strip/replace/split/join/find/count/startswith/endswith/isdigit/isalpha`.
- Real back-end vazifalarini bajaradi: foydalanuvchi kiritgan ma'lumotni tozalash va tekshirish (validatsiya).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Ro'yxatdan o'tish formasiga foydalanuvchilar nima yozadi: `"  AZIZ@Mail.UZ "`, `"+998 (90) 123-45-67"`, `"aziz   karimov"`. *"Back-end dasturchi bu 'axlat'ni tozalab, bazaga toza holda saqlashi kerak. Bugun shuni o'rganamiz."* |
| 5–10 | **Takrorlash** | 6-dars: o'quvchilar bir-birining "xatoli dasturi"ni almashib, 3 daqiqada yechadi |
| 10–25 | **Yangi mavzu** | Indekslash, kesish, immutable, metodlar (jadval), `in` operatori, satr bo'ylab `for` |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Ma'lumot tozalovchi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod
```python
s = "  Salom, Dunyo!  "
print(s.strip())            # "Salom, Dunyo!"
print(s.strip().lower())    # "salom, dunyo!"
print(s.strip()[0:5])       # "Salom"
print(s.strip()[::-1])      # "!oynuD ,molaS"

email = "  AZIZ@Mail.UZ "
email = email.strip().lower()           # "aziz@mail.uz"
print("@" in email and email.endswith(".uz"))

tel = "+998 (90) 123-45-67"
toza = "".join(c for c in tel if c.isdigit())   # "998901234567"

ism = "aziz   karimov"
print(" ".join(ism.split()).title())    # "Aziz Karimov"
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10
