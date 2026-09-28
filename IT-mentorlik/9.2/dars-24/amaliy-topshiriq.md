# 24-dars amaliy topshiriq: AI yordamchi bot 🤖

```bash
pip install google-genai
```
`.env` ga `GEMINI_API_KEY` qo'shing (namuna: `kod/.env.example`). Namuna kod: `kod/ai_bot.py`.

## 🟢 Oson (+10 XP)
Bot ishlaydi: har qanday savolga Gemini orqali javob beradi. `ChatAction.TYPING` ("yozmoqda..." belgisi) ko'rinadi.

## 🟡 O'rta (+10 XP)
**O'z system prompt'ingizni** yozing. Botingiz kim bo'ladi? G'oyalar:
- 🇬🇧 Ingliz tili suhbatdoshi (xatolarni muloyim tuzatadi)
- 📐 Matematika yordamchisi (javobni emas, yo'lni ko'rsatadi)
- 🏛 O'zbekiston tarixi gidi
- 🍳 Oshpaz (mavjud masalliqlardan retsept)
System prompt'da: rol, til, uslub, cheklovlar, javob uzunligi.

## 🔴 Qiyin (+20 XP)
- Suhbat tarixi (`chats.create`) + `/reset`
- Rate limit (har foydalanuvchiga 5 soniyada 1 so'rov) va kunlik limit (masalan, 30 ta savol)
- Rasm yuborilsa, AI uni tahlil qilsin (Gemini multimodal: rasm baytlarini `types.Part.from_bytes(...)` bilan yuborish)
