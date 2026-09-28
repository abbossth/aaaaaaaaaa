# 9-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `{}` bo'sh set deb o'ylash | `{}` — bo'sh dict! Bo'sh set: `set()` |
| `d["kalit"]` → KeyError | `.get()` yoki `if k in d` |
| Dict ustida aylanishda uni o'zgartirish → `RuntimeError` | `for k in list(d):` |
| f-string ichida dict: `f"{m["tel"]}"` → SyntaxError (Python 3.11 va eski versiyalarda) | Ichida boshqa qo'shtirnoq: `f"{m['tel']}"` |

## Maslahat
- "Kontaktlar kitobi" — I bob davomidagi uzluksiz loyiha: v1 (dict) → v2 (funksiyalar, 10-dars) → v3 (fayl + try/except, 11-dars) → 13-darsdagi jamoaviy CLI loyihaga asos. O'quvchilar kodini saqlab borishini nazorat qiling.
- 13-darsdan keyin (OOP) uni klasslarga, 36-darsda esa PostgreSQL + botga o'tkazish mumkin.
