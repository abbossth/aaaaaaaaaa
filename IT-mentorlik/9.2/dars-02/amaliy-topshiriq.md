# 2-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. `python-kurs` papkasini yarating va uni VS Code'da oching.
2. Terminalda (`Ctrl+\``) virtual muhit yarating va uni faollashtiring. Terminal satri boshida `(.venv)` paydo bo'lishi kerak.
3. `salom.py` faylini yarating va ichiga 3 qator yozing: ismingiz, sinfingiz, sevimli dasturlash tilingiz. Terminaldan `python salom.py` bilan ishga tushiring.

## 🟡 O'rta (+10 XP)
4. Python REPL'da (`python` buyrug'i) kalkulyator sifatida hisoblang:
   - `2 ** 100`: qanday son chiqdi? (Python katta sonlardan qo'rqmaydi!)
   - `import this`: "Zen of Python"ni o'qing va eng yoqqan 2 qatorini tarjima qiling.
5. `pip install rich` qilib, `kod/rich_salom.py` misolini ishga tushiring.

## 🔴 Qiyin (+20 XP)
6. `pip freeze > requirements.txt` qiling. Yangi papkada yangi venv yarating va `pip install -r requirements.txt` bilan xuddi shu kutubxonalarni o'rnating. Bu nima uchun foydali? (Javob: jamoadoshingiz yoki server aynan sizdagi versiyalarni o'rnata oladi.)
7. `.gitignore` faylini yarating va unga `.venv/` qo'shing. Nega venv GitHub'ga yuklanmaydi?

---
## Javoblar
- 4: `2**100 = 1267650600228229401496703205376`
- 7: venv katta hajmli (yuzlab MB) va har bir kompyuterda o'zi yaratiladi. Uning o'rniga `requirements.txt` yuklanadi.
