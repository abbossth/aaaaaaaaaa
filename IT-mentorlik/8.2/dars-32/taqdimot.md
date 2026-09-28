# 32-dars slaydlari: Bug Hunt 🐛

## 1-slayd
🦋 1947-yil: Harvard Mark II ichidan **haqiqiy kuya** topildi → "bug" so'zi shundan

## 2-slayd — 3 xil xato
| Tur | Qachon? | Misol |
|---|---|---|
| Sintaksis | Dastur umuman ishlamaydi | `if x > 5` (`:` yo'q) |
| Runtime | Ishlayotganda qulaydi | `int("abc")`, `lst[10]`, `1/0` |
| Mantiqiy | Ishlaydi, lekin natija noto'g'ri | `range(1, 10)` o'rniga `range(1, 11)` kerak edi |

## 3-slayd — Traceback'ni o'qish (pastdan yuqoriga!)
```
Traceback (most recent call last):
  File "bank.py", line 12, in <module>
    h.yechish(500)
  File "bank.py", line 7, in yechish
    self.balans -= sumaa
NameError: name 'sumaa' is not defined
```
1️⃣ Oxirgi qator: **xato turi va sababi** · 2️⃣ Uning ustida: **qaysi qator**

## 4-slayd — Eng ko'p uchraydigan xatolar
`NameError` · `TypeError` · `IndexError` · `KeyError` · `ValueError` · `ZeroDivisionError` · `IndentationError` · `AttributeError`

## 5-slayd — Debugger
VS Code: qator raqami yonini bosing 🔴 (breakpoint) → **F5** → **F10** (Step Over) → chapda o'zgaruvchilar qiymati ko'rinadi

## 6-slayd — Qoida
> "Taxmin qilma — **tekshir**." `print(f"{x=}")` — eng oddiy debugger
