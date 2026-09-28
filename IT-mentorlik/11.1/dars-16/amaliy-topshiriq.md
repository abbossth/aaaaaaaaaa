# 16-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. `kod/todo-api` ni ishga tushiring: `npm install` → `npm run dev`. Postman'da barcha 5 ta endpoint'ni sinab ko'ring. Kolleksiyaga qo'shing.
2. `npm test`: hammasi yashilmi?

## 🟡 O'rta (+10 XP)
3. Todo'ga `priority` maydoni qo'shing (`low | medium | high`, default `medium`). Validatsiya: boshqa qiymat → 400.
4. `GET /api/todos?priority=high&sort=createdAt` — filtrlash va saralash.
5. Har bir yangi funksiya uchun Supertest test yozing.

## 🔴 Qiyin (+20 XP)
6. **Pagination:** `GET /api/todos?page=2&limit=5` → `{ data, total, page, limit, totalPages }`.
7. Ma'lumotni `todos.json` faylida saqlang (server qayta ishga tushsa ham yo'qolmasin). `fs/promises` va `async/await`.
8. Kodni qatlamlarga ajrating: `routes/todos.js` (Router), `services/todoService.js` (mantiq), `app.js`. SRP!
