# Kutubxona API — namuna javob

| Harakat | Metod | URL | Status | Xatolar |
|---|---|---|---|---|
| Barcha kitoblar | GET | `/books?page=1&limit=20` | 200 | 400 (noto'g'ri page) |
| Janr bo'yicha | GET | `/books?genre=roman` | 200 | — |
| Bitta kitob | GET | `/books/:id` | 200 | 404 |
| Yangi kitob | POST | `/books` | 201 | 400/422 (validatsiya), 401 |
| Qisman yangilash | PATCH | `/books/:id` | 200 | 404, 422 |
| O'quvchi ijaralari | GET | `/students/:id/loans` | 200 | 404 |
| Ijaraga berish | POST | `/loans` (body: `bookId`, `studentId`) | 201 | 404, 409 (kitob band) |
| Qaytarish | PATCH | `/loans/:id` (body: `{"returnedAt": "..."}`) yoki `POST /loans/:id/return` | 200 | 404, 409 (allaqachon qaytarilgan) |

Izoh: "qaytarish" kabi harakatlarni REST'da ifodalashning bir nechta to'g'ri usuli bor. Muhimi — izchillik va asoslash.
