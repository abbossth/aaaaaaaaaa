# 16-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `req.body` — `undefined` | `app.use(express.json())` yo'q yoki Postman'da body "raw → JSON" emas |
| `req.params.id` satr: `todos.find(t => t.id === req.params.id)` topmaydi | `Number(req.params.id)` |
| "Cannot set headers after they are sent" | Bitta so'rovga ikki marta `res.json()`. `return res.json(...)` |
| `EADDRINUSE: 3000` | Server allaqachon ishlayapti. Eskisini to'xtating yoki portni o'zgartiring |

## Maslahat
- `createApp()` fabrika funksiyasi (12-dars, Factory!) testlarda har safar toza ilova olish uchun. Buni o'quvchilarga ta'kidlang.
- Express 5 chiqqan bo'lsa ham, ko'pchilik qo'llanmalar Express 4 da. Loyihada 4-versiya ishlatildi.
- `node --watch` Node 18.11+ da ishlaydi (nodemon kerak emas).
