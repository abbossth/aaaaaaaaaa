# 16-dars challenge: "API almashinuvi" 🔄

**Vaqt:** 14 daqiqa | **Format:** juftliklar

1. Juftlik A o'z API'sini ishga tushiradi (bir xil Wi-Fi tarmog'ida). Terminalda `ipconfig` bilan IP'ni topadi. Server `0.0.0.0` da tinglashi kerak.
2. Juftlik B faqat **Postman** orqali A'ning API'sini "buzishga" harakat qiladi:
   - bo'sh body, noto'g'ri JSON, `title: 12345`, juda uzun title (10 000 belgi)
   - mavjud bo'lmagan ID, `id = abc`, manfiy ID
   - noma'lum route, noto'g'ri metod (`PUT /api/todos`)
3. Har bir **500 xato** yoki **qulash** — B'ga +5. Barcha holatlarda to'g'ri 4xx qaytgan bo'lsa — A'ga +20.
4. Rollar almashadi.

**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5 · "Bulletproof API" 🛡 badge
