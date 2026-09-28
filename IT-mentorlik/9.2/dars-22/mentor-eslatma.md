# 22-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| Holatli handler ishlamaydi, echo handler ushlab qoladi | Handler'lar **tartibi** muhim: holatli handler'lar umumiy echo'dan **oldin** |
| `/cancel` ishlamaydi, holat handler'i uni "ism" deb qabul qiladi | `/cancel` handler'ini holatlardan oldin ro'yxatdan o'tkazing |
| Bot qayta ishga tushsa, holatlar yo'qoladi | Standart `MemoryStorage`. Production'da Redis storage (keyinroq) |
| `message.contact` — `None` | Foydalanuvchi raqamni qo'lda yozgan. `F.contact` filtri va alohida "noto'g'ri" handler |

## Maslahat
FSM diagrammasini doskaga albatta chizing. Vizual ko'rinish koddan ko'ra ancha tushunarliroq.
