# 4-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `IndentationError` | VS Code'da Tab = 4 probel ekanini tekshiring. Tab va probelni aralashtirmang |
| `if x = 5:` | `SyntaxError`. Taqqoslash `==` bilan |
| `if tarif == "ekonom" or "komfort":` | Har doim True bo'ladi! To'g'ri: `tarif in ("ekonom", "komfort")` |
| elif tartibi noto'g'ri (kichik shart birinchi) | Baho misolida ko'rsating |
| `input` natijasini `int` ga o'girmasdan taqqoslash: `"9" > "10"` → True | Satrlar alifbo bo'yicha taqqoslanadi |

## Maslahat
`or "komfort"` xatosi — Python'dagi eng klassik xatolardan biri. Uni albatta ekranda "tuzoq" sifatida ko'rsating: `if x == 1 or 2:` har doim ishlaydi. Nega? (`2` truthy)
