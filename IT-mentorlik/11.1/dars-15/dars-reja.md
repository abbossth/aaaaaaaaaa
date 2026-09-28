# 15-dars. HTTP, REST, JSON, status kodlar, Postman

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "REST API va JSON asoslari"

## Maqsad
- HTTP so'rov va javob tuzilishini biladi: metod, URL, header'lar, body, status kod.
- HTTP metodlari semantikasini tushunadi: GET, POST, PUT, PATCH, DELETE va idempotentlik.
- REST tamoyillari asosida resursga yo'naltirilgan URL loyihalaydi: `/users/42/orders`.
- JSON tuzilmasini (obyekt, massiv, turlar) va status kodlar guruhlarini (2xx, 3xx, 4xx, 5xx) biladi.
- **Postman** (yoki Thunder Client) bilan real API'larni sinaydi: query parametrlar, header, body, pagination.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Brauzerda `F12` → Network → istalgan saytni ochish → bitta so'rovni tahlil qilish. *"Har bir tugma bosilganda ortda shunday 'xat' ketadi. Bugun bu xatlarni o'qish va yozishni o'rganamiz."* |
| 5–10 | **Takrorlash** | 13-dars testi |
| 10–28 | **Yangi mavzu** | HTTP anatomiyasi. Metodlar. Status kodlar. REST URL dizayni. JSON. Pagination va filtrlash (`?page=2&limit=10&sort=-price`) |
| 28–38 | **Jonli** | Postman: `jsonplaceholder.typicode.com` bilan GET/POST/PUT/DELETE. `dummyjson.com` bilan login (token olish) |
| 38–62 | **Amaliyot** | `amaliy-topshiriq.md`: Postman kolleksiyasi |
| 62–75 | **Challenge** | `challenge.md`: "REST arxitektori" |
| 75–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Postman kolleksiyasi +5/+10/+20 · Challenge +20/+10/+5
