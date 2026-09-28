# 15-dars amaliy topshiriq: Postman kolleksiyasi

Postman o'rnating (postman.com) yoki VS Code'da **Thunder Client** kengaytmasi. Kolleksiya nomi: `11.1 — REST mashqlari`.

## 🟢 Oson (+5 XP): jsonplaceholder.typicode.com
1. `GET /posts` — nechta post bor?
2. `GET /posts/1` — 1-post sarlavhasi?
3. `GET /posts/1/comments` — nechta izoh?
4. `GET /posts?userId=3` — 3-foydalanuvchining postlari
5. `GET /posts/9999` — qaysi status kod?

## 🟡 O'rta (+10 XP): yozish so'rovlari
6. `POST /posts` body bilan: `{"title": "Salom", "body": "11.1 dan", "userId": 1}`. Status kod va javob?
7. `PUT /posts/1` va `PATCH /posts/1` (faqat `title`). Javoblar farqi?
8. `DELETE /posts/1`. Status kod?

## 🔴 Qiyin (+20 XP): dummyjson.com (autentifikatsiya)
9. `POST https://dummyjson.com/auth/login` body: `{"username": "emilys", "password": "emilyspass"}` → `accessToken` ni oling.
10. `GET https://dummyjson.com/auth/me` — header: `Authorization: Bearer <token>`. Token'siz yuborsangiz nima bo'ladi?
11. Postman **environment** o'zgaruvchisi (`{{baseUrl}}`, `{{token}}`) yarating va login so'rovining **Tests** (Post-response) bo'limida token'ni avtomatik saqlang:
```js
pm.environment.set("token", pm.response.json().accessToken);
```
12. `GET https://dummyjson.com/products?limit=5&skip=10&select=title,price` — pagination qanday ishlaydi?

Kolleksiyani eksport qilib (JSON), jamoa reposiga `docs/postman/` ga qo'shing.
