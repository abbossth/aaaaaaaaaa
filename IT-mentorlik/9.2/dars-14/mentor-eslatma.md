# 14-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `self` unutilgan: `def ortacha():` → TypeError "takes 0 positional arguments but 1 was given" | Metodning birinchi parametri doim `self` |
| `__init__` o'rniga `_init_` yoki `__int__` | Ikki pastki chiziq, "init" |
| Atributda `self.` unutilgan: `ism = ism` | Lokal o'zgaruvchi bo'lib qoladi, obyektga saqlanmaydi |
| Class atributi ro'yxat (`baholar = []`) → hamma obyektda bir xil ro'yxat! | Klassik tuzoq. Ro'yxat `__init__` ichida bo'lishi kerak |

## Maslahat
- pythontutor.com'da `talaba.py` ni vizual ko'rsating: obyektlar va `self` qanday bog'lanishi yaqqol ko'rinadi.
- Class atributidagi ro'yxat tuzog'ini albatta jonli ko'rsating. Bu intervyularda ham so'raladi.
