# 15-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `__str__` `print` qiladi, lekin `return` qilmaydi | `TypeError: __str__ returned non-string` |
| `sum(pullar)` → TypeError (`0 + Pul`) | Boshlang'ich qiymat: `sum(pullar, Pul(0))` yoki `__radd__` |
| `__eq__` yozilgach, obyekt set/dict kaliti bo'lolmay qoladi | `__hash__` kerak (kuchli o'quvchilar uchun) |
| `@classmethod` ichida `Talaba(...)` qattiq yozilgan | `cls(...)` yaxshiroq (meros uchun) |

## Maslahat
"Pul" klassi — real fintech amaliyoti. Click/Payme'da pul summalari tiyinlarda (butun son) saqlanishini aytib qo'ying. Bu qiziqish uyg'otadi.
