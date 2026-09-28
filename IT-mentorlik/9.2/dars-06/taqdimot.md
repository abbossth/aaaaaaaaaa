# 6-dars slaydlari: Bug Hunt

## 1-slayd
🐞 **BUG HUNT #1** · 9.2 🆚 9.3

## 2-slayd — Birinchi "bug"
1947-yil, Harvard Mark II kompyuteri ichidan haqiqiy kuya topildi 🦋
Grace Hopper jurnalga yozgan: *"First actual case of bug being found"*

## 3-slayd — Qimmat xatolar
🚀 Ariane 5 (1996): son turi to'lib ketdi → 370 mln $
🛰 Mars Climate Orbiter (1999): dyuym va metr chalkashligi → 125 mln $
💸 Knight Capital (2012): noto'g'ri deploy → 45 daqiqada 440 mln $

## 4-slayd — Xatolarning 3 turi
1️⃣ **Sintaksis:** Python kodni tushunmaydi (`SyntaxError`, `IndentationError`)
2️⃣ **Bajarilish (runtime):** ishlash vaqtida qulaydi (`TypeError`, `ValueError`, `ZeroDivisionError`, `NameError`)
3️⃣ **Mantiqiy:** ishlaydi, lekin natija noto'g'ri 😈 (eng xavflisi!)

## 5-slayd — Traceback'ni o'qish
```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(yosh + 1)
TypeError: can only concatenate str (not "int") to str
```
⬇️ Pastdan boshlang: **xato turi** → **xabar** → **qator raqami**

## 6-slayd — Debug usullari
🖨 `print()` bilan qiymatlarni chiqarish
🔴 VS Code: breakpoint (qator chapiga bosish) → F5 → F10 qadamma-qadam
🦆 **Rubber duck debugging:** kodni o'rdakchaga (yoki sherigingizga) qatorma-qator tushuntiring
