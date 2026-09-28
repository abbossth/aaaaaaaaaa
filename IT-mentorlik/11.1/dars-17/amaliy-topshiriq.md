# 17-dars amaliy topshiriq

## 🟢 Oson (+10 XP): Auth API
1. `todo-api` ga `npm i jsonwebtoken bcrypt cors` qiling va `kod/auth.js` ni ulang.
2. Postman'da: register → login → token'ni environment'ga saqlash → `GET /api/me` (token bilan va token'siz).
3. jwt.io'da o'z token'ingizni oching: payload'da nima bor?

## 🟡 O'rta (+10 XP): React ulanishi
4. Vite bilan React ilova yarating va `kod/App.jsx` ni moslang.
5. Login → todolar ro'yxati → yangi todo qo'shish ishlasin.
6. CORS xatosini ataylab chiqaring (cors'ni o'chirib) va Console'dagi xabarni o'qing. Keyin tuzating.

## 🔴 Qiyin (+20 XP)
7. Har bir todo o'z egasiga tegishli bo'lsin (`userId`). Foydalanuvchi faqat o'z todolarini ko'radi va o'zgartiradi (boshqasiniki → 404 yoki 403).
8. `requireRole("admin")` bilan `GET /api/admin/users` endpoint'i.
9. `JWT_SECRET` ni `.env` fayliga chiqaring (`node --env-file=.env`) va `.env` ni `.gitignore` ga qo'shing.
