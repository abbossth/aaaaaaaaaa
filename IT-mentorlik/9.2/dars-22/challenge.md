# 22-dars challenge: "Pitsa buyurtmasi" 🍕

**Vaqt:** 17 daqiqa | **Format:** juftlik

FSM bilan pitsa buyurtma boti:
1. `/order` → **o'lcham** (inline: Kichik 45k / O'rta 65k / Katta 85k)
2. → **qo'shimchalar** (inline, **bir nechtasini** tanlash mumkin: 🧀 +8k, 🍄 +6k, 🌶 +3k, ✅ Tayyor)
3. → **manzil** (matn, kamida 10 belgi) yoki 📍 lokatsiya tugmasi (`request_location=True`)
4. → **tasdiq**: chek (o'lcham, qo'shimchalar, manzil, jami summa) + ✅/❌

**Maslahat:** tanlangan qo'shimchalarni ro'yxat sifatida saqlang: `data.get("qoshimcha", [])`. Qayta bosilsa, olib tashlansin (toggle), tugmada ✔ belgisi bilan ko'rsatilsin.

**XP:** ishlaydigan birinchi 3 juftlik +30/+20/+10
