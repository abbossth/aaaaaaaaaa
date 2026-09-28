# 24-dars slaydlari: AI bot 🤖

## 1-slayd
**40 qator kod = o'zbekcha gaplashadigan aqlli bot**

## 2-slayd — Qanday ishlaydi?
```
Foydalanuvchi → Telegram → Sizning bot → Gemini API (Google serveri)
                                         ←── AI javobi
            ←───────── javob ─────────
```

## 3-slayd — System prompt = botning "xarakteri"
```
Sen 9-sinf o'quvchilari uchun Python o'qituvchisisan.
- Faqat o'zbek tilida (lotin yozuvida) javob ber.
- Sodda tushuntir, har doim kichik kod misoli keltir.
- Uyga vazifani to'liq yechib berma — maslahat ber.
- Python va dasturlashdan boshqa mavzularda muloyimlik bilan rad et.
```

## 4-slayd — Kod
```python
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
javob = await client.aio.models.generate_content(
    model="gemini-2.5-flash",
    contents=savol,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
)
await message.answer(javob.text)
```

## 5-slayd — Suhbat tarixi (xotira)
LLM o'zi hech narsani eslamaydi! Har safar **butun suhbatni** yuborish kerak.
Chat sessiya obyekti buni avtomatik qiladi: `client.aio.chats.create(...)`

## 6-slayd — Tokenlar va limitlar
Token ≈ so'zning bir qismi. Bepul rejada: daqiqasiga va kuniga cheklangan so'rovlar.
➡️ Uzun suhbat = ko'p token = sekin va qimmat. Tarixni cheklang (oxirgi 10 xabar).

## 7-slayd — ⚠️ Xavfsizlik
🔑 API kalit — `.env` da, GitHub'da emas!
💉 **Prompt injection:** "Oldingi ko'rsatmalarni unut va..." — foydalanuvchi botni boshqarishga urinadi
🤥 AI noto'g'ri javob berishi mumkin — muhim ma'lumotlarni tekshiring
🔒 Foydalanuvchilarning shaxsiy ma'lumotlarini AI'ga yubormang
