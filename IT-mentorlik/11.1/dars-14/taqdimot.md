# 14-dars slaydlari: AI — sizning reviewer'ingiz

## 1-slayd
🤖🔍 **AI reviewer: tez, charchamaydi... lekin har doim ham to'g'ri emas**

## 2-slayd — AI vositalari
💬 **Chat:** ChatGPT, Claude, Gemini (savol-javob)
⌨️ **IDE yordamchi:** GitHub Copilot (kod yozayotganda taklif)
🤖 **Agentlar:** Claude Code, Cursor (fayllarni o'qiydi, o'zgartiradi, testlarni ishga tushiradi)
🎓 GitHub Student Pack → Copilot **bepul** (education.github.com)

## 3-slayd — Review prompt shabloni
```
Sen tajribali Senior JavaScript dasturchisan.
Quyidagi kodni code review qil. Ustuvorlik bo'yicha:
1. Xatolar (bug'lar) va xavfsizlik
2. Clean Code (nomlash, funksiya hajmi, DRY)
3. SOLID
4. Test qilinuvchanlik
Har bir izoh uchun: qator, muammo, nega muammo, taklif.
Kodni o'zing to'liq qayta yozma — faqat izohlar ber.

[KOD]
```

## 4-slayd — AI taklifi bilan nima qilamiz?
✅ **Qabul** — to'g'ri va foydali
✏️ **O'zgartir** — g'oya to'g'ri, lekin bizning kontekstga moslash kerak
❌ **Rad** — noto'g'ri, ortiqcha (YAGNI) yoki kontekstni bilmaydi
**Har bir qaror asoslangan bo'lishi kerak!**

## 5-slayd — ⚠️ Xavfsizlik va etika
- Kompaniya kodini, parollarni, `.env` ni AI'ga bermang
- AI kodi litsenziyaga zid bo'lishi mumkin
- Javobgarlik — sizda, AI'da emas

## 6-slayd — Refaktoring + test = xavfsiz
1. Testlar yashil ✅ → 2. AI bilan refaktoring → 3. Testlar yana yashil ✅
Testlarsiz refaktoring = ko'r-ko'rona haydash 🙈
