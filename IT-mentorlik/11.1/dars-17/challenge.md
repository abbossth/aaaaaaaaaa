# 17-dars challenge: "Token o'g'risi" 🕵️ (xavfsizlik muhokamasi)

**Vaqt:** 10 daqiqa | **Format:** jamoalar

Mentor 5 ta "xavfsizlik holati"ni o'qiydi. Jamoalar: **xavfli** yoki **xavfsiz**, va nega?

| № | Holat | Javob |
|---|---|---|
| 1 | JWT payload'ga `{ userId: 1, password: "12345" }` qo'yilgan | ❌ Payload hammaga ko'rinadi |
| 2 | `JWT_SECRET = "secret"` GitHub'ga push qilingan | ❌ Har kim o'zi token yasay oladi |
| 3 | Login xatosida: "Bunday email yo'q" / "Parol xato" deb alohida xabar | ⚠️ Hujumchi qaysi email'lar ro'yxatdan o'tganini biladi |
| 4 | Token muddati: 1 soat | ✅ O'g'irlansa ham tez yaroqsiz bo'ladi |
| 5 | `cors({ origin: "*" })` + cookie bilan auth | ❌ Istalgan sayt so'rov yubora oladi |
| 6 | Parollar `bcrypt` bilan hash'langan | ✅ |

**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
