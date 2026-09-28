# 16-dars slaydlari: Express REST API

## 1-slayd
🚂 **Express — Node.js'ning eng mashhur web freymvorki**

## 2-slayd — 10 qatorlik server
```js
import express from "express";
const app = express();
app.use(express.json());

app.get("/api/hello", (req, res) => {
  res.json({ message: "Salom, 11.1!" });
});

app.listen(3000, () => console.log("http://localhost:3000"));
```

## 3-slayd — So'rovdan ma'lumot olish
`GET /todos/42` → `req.params.id` = "42"
`GET /todos?done=true` → `req.query.done` = "true"
`POST /todos` + JSON body → `req.body.title`

## 4-slayd — Javob
```js
res.status(201).json(todo);     // yaratildi
res.status(404).json({ error: { code: "NOT_FOUND", message: "Topilmadi" } });
res.status(204).end();          // o'chirildi, body yo'q
```

## 5-slayd — Middleware = konveyer 🏭
```
So'rov → [json parser] → [logger] → [auth] → [route handler] → Javob
                                                      ↓ xato
                                               [error handler]
```
```js
app.use((req, res, next) => { console.log(req.method, req.url); next(); });
```

## 6-slayd — Xato ishlovchisi
```js
app.use((err, req, res, next) => {
  res.status(err.status || 500).json({ error: { code: err.code || "INTERNAL", message: err.message } });
});
```
4 ta parametr = Express buni error handler deb taniydi
