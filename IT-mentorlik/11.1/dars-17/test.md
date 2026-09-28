# 17-dars tezkor test

1. Autentifikatsiya va avtorizatsiya farqi? — Authn "kimsiz?", authz "nimaga ruxsatingiz bor?"
2. JWT'ning 3 qismi? — Header, payload, signature
3. JWT payload shifrlanganmi? — Yo'q, faqat imzolangan (base64 bilan kodlangan)
4. Parolni saqlashning to'g'ri usuli? — bcrypt (yoki argon2) bilan hash
5. Token qaysi header'da yuboriladi? — `Authorization: Bearer <token>`
6. CORS kim tomonidan tekshiriladi? — Brauzer
7. 401 va 403 qachon? — 401 token yo'q/yaroqsiz, 403 token bor lekin ruxsat yo'q
