# 24-dars mentor eslatmasi

- **Model nomi o'zgaradi.** Dars kuni aistudio.google.com'da joriy bepul modelni tekshiring va `.env` dagi `GEMINI_MODEL` ni moslang.
- Google AI Studio'da yosh va mamlakat bo'yicha cheklovlar bo'lishi mumkin. Muammo bo'lsa: mentor bitta "dars kaliti" yaratadi, dars tugagach uni o'chiradi (revoke).
- Bepul rejada limitlar mavjud. 25 ta o'quvchi bir vaqtda so'rov yuborsa, limit tugashi mumkin. Rate limit shu uchun kerak.
- `google-genai` — Google'ning yangi rasmiy SDK'si (eski `google-generativeai` emas). Internetdagi eski misollar chalkashtirishi mumkin.
- Prompt injection challenge'i juda qiziqarli va xavfsizlik bo'yicha muhim saboq beradi. Uni tashlab ketmang.
