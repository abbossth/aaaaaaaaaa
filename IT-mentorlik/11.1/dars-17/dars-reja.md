# 17-dars. JWT autentifikatsiya, CORS, React frontendni API'ga ulash

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "REST API... autentifikatsiya (Bearer/JWT) va CORS asoslari"

## Maqsad
- Autentifikatsiya (kimsiz?) va avtorizatsiya (nimaga ruxsatingiz bor?) farqini biladi.
- JWT tuzilishini (header.payload.signature) va Bearer token oqimini tushunadi.
- Parollarni `bcrypt` bilan hash qiladi. Hech qachon ochiq saqlamaydi.
- Express'da `/auth/register`, `/auth/login` va himoyalangan route'lar uchun `auth` middleware yozadi.
- CORS nima ekanini va nega brauzer boshqa domenga so'rovni bloklashini tushunadi, `cors` middleware'ni sozlaydi.
- React (Vite) ilovasidan `fetch` bilan API'ga ulanadi: login → token → himoyalangan ma'lumot.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | jwt.io saytiga istalgan JWT'ni qo'yish: ichidagi ma'lumot ko'rinadi! *"JWT shifrlanmagan — u imzolangan. Farqi nima? Bugun bilib olamiz."* |
| 5–10 | **Takrorlash** | 16-dars testi |
| 10–25 | **Yangi mavzu** | Authn vs Authz. Parol hash (bcrypt, salt). JWT oqimi (sxema). CORS: "brauzer qo'riqchisi" |
| 25–40 | **Jonli kod** | `kod/auth.js`: register, login, auth middleware. Postman: token bilan va token'siz |
| 40–65 | **Amaliyot** | `amaliy-topshiriq.md`: React + API |
| 65–75 | **Challenge** | `challenge.md`: "Token o'g'risi" (xavfsizlik muhokamasi) |
| 75–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Auth API +10 · React ulanishi +10 · Qiyin daraja +20 · Challenge +20/+10/+5
