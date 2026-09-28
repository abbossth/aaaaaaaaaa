# 15-dars slaydlari: HTTP va REST

## 1-slayd
✉️ **HTTP = client va server o'rtasidagi xat**

## 2-slayd — So'rov (request)
```
POST /api/orders?promo=MAKTAB10 HTTP/1.1     ← metod, yo'l, query
Host: shop.uz
Content-Type: application/json               ← header'lar
Authorization: Bearer eyJhbGciOi...

{"productId": 42, "qty": 2}                  ← body
```

## 3-slayd — Javob (response)
```
HTTP/1.1 201 Created                         ← status
Content-Type: application/json

{"id": 1001, "status": "new", "total": 5800000}
```

## 4-slayd — Metodlar
| Metod | Ma'nosi | Idempotent? |
|---|---|---|
| GET | O'qish | ✅ |
| POST | Yaratish | ❌ |
| PUT | To'liq almashtirish | ✅ |
| PATCH | Qisman o'zgartirish | (odatda) ❌ |
| DELETE | O'chirish | ✅ |
Idempotent = 10 marta yuborsangiz ham natija 1 martadagidek

## 5-slayd — Status kodlar
2xx ✅ `200 OK` · `201 Created` · `204 No Content`
3xx ↪️ `301 Moved` · `304 Not Modified`
4xx 🙋 (client xatosi) `400 Bad Request` · `401 Unauthorized` · `403 Forbidden` · `404 Not Found` · `422 Unprocessable`
5xx 💥 (server xatosi) `500 Internal Server Error` · `503 Unavailable`

## 6-slayd — REST URL dizayni
✅ `GET /products` · `GET /products/42` · `POST /products` · `PATCH /products/42` · `DELETE /products/42`
✅ `GET /users/7/orders` · `GET /products?category=phone&page=2&limit=20`
❌ `/getAllProducts` · `/deleteProduct?id=42` · `/products/delete/42`
**Ot (resurs) — ko'plikda, fe'l — HTTP metodida!**

## 7-slayd — Xato formati (bir xil bo'lsin!)
```json
{ "error": { "code": "VALIDATION_ERROR", "message": "Email noto'g'ri", "field": "email" } }
```
