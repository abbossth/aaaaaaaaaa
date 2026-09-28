# 17-dars slaydlari: JWT, CORS, React

## 1-slayd
🔐 **Kimsiz? (autentifikatsiya) · Nimaga ruxsatingiz bor? (avtorizatsiya)**

## 2-slayd — Parollarni saqlash
❌ `password: "12345"` (ochiq)
❌ `md5("12345")` (tez buziladi)
✅ `bcrypt.hash("12345", 10)` → `$2b$10$N9qo8uLOickgx2ZMRZoMye...`
Salt + sekin algoritm = xavfsiz

## 3-slayd — JWT tuzilishi
`eyJhbGciOi...` **.** `eyJ1c2VySWQiOjF9` **.** `SflKxwRJSMeKKF2QT4fw...`
header (algoritm) · payload (userId, rol, muddat) · signature (imzo)
⚠️ Payload **shifrlanmagan**! Maxfiy ma'lumot qo'ymang

## 4-slayd — Oqim
```
1. POST /auth/login {email, parol}  →  server parolni tekshiradi
2. ←  { token: "eyJ..." }
3. GET /api/todos
   Authorization: Bearer eyJ...     →  server imzoni tekshiradi
4. ←  200 (yoki 401)
```

## 5-slayd — Auth middleware
```js
function auth(req, res, next) {
  const token = req.headers.authorization?.split(" ")[1];
  if (!token) return res.status(401).json({ error: { code: "NO_TOKEN" } });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    res.status(401).json({ error: { code: "INVALID_TOKEN" } });
  }
}
app.get("/api/me", auth, (req, res) => res.json(req.user));
```

## 6-slayd — CORS 🛂
Brauzer: *"localhost:5173 (React) localhost:3000 (API)ga so'rov yubormoqchi. Server ruxsat berganmi?"*
```js
import cors from "cors";
app.use(cors({ origin: "http://localhost:5173" }));
```
CORS — **brauzer** qoidasi. Postman'da CORS yo'q!

## 7-slayd — React'dan so'rov
```jsx
const res = await fetch("http://localhost:3000/api/todos", {
  headers: { Authorization: `Bearer ${token}` },
});
const data = await res.json();
```
