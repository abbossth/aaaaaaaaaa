# 16-dars. Express bilan REST API: CRUD, xatolar formati

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "REST API va JSON asoslari" (JS/Express'ga moslashtirilgan)

## Maqsad
- Express.js bilan server yaratadi: `app.get/post/put/patch/delete`, `req.params`, `req.query`, `req.body`, `res.status().json()`.
- Middleware tushunchasini biladi: `express.json()`, logger, xato ishlovchisi (error handler).
- To'liq CRUD API yozadi (hozircha xotirada saqlanadi) va 15-darsdagi REST qoidalariga amal qiladi.
- Yagona xato formatini va to'g'ri status kodlarni qo'llaydi (400, 404, 201, 204).
- API'ni Postman bilan sinaydi va Vitest + Supertest bilan birinchi integratsion testni yozadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"15-darsda boshqalarning API'sidan foydalandingiz. Bugun o'z API'ingizni yozasiz va jamoadoshingiz unga Postman'dan so'rov yuboradi."* |
| 5–10 | **Takrorlash** | 15-dars testi |
| 10–30 | **Jonli kod** | `kod/todo-api` ni noldan: `npm init`, express, GET/POST → Postman → GET/:id, 404 → PATCH/DELETE → middleware → error handler |
| 30–60 | **Amaliyot** | `amaliy-topshiriq.md` |
| 60–74 | **Challenge** | `challenge.md`: "API almashinuvi" |
| 74–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
