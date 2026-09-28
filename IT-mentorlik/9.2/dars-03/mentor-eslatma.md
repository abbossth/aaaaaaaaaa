# 3-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Tushuntirish |
|---|---|
| `TypeError: can only concatenate str (not "int") to str` | `input()` natijasini `int()` ga o'girish esdan chiqqan |
| `ValueError: invalid literal for int()` | Foydalanuvchi son o'rniga matn yoki `3.5` kiritgan. Kelajakda `try/except` bilan tutamiz (11-dars) |
| f-string'da `f` harfi unutilgan: `"{ism}"` | Natijada figurali qavslar bilan matn chiqadi |
| O'zgaruvchi nomida probel yoki tire | `SyntaxError` |
| `print(f"{narx:,.2f}")` o'rniga `print(f"{narx:.2f,}")` | Tartib muhim: avval `,`, keyin `.2f` |

## Maslahatlar
- `bool("0") == True` darsning "wow" lahzasi, uni albatta ko'rsating.
- Soniya konvertori (5-topshiriq) `//` va `%` ni mustahkamlaydi. Bu keyinroq pagination va vaqt hisoblashda juda kerak bo'ladi.
- Chek challenge'ida hali `if` o'tilmagan. Bonusni `if` bilan qilganlarni rag'batlantiring.
