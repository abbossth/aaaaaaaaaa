# 26-dars amaliy topshiriq

Cheat-sheet: `kod/cheatsheet.md`

## 🟢 Oson (+5 XP): Navigatsiya va fayllar
Faqat terminal bilan (sichqonchasiz!):
1. Uy papkangizda `devops-kurs/loyiha/{src,tests,docs}` tuzilmasini bitta buyruq bilan yarating (`mkdir -p` + `{}`).
2. `src/app.py`, `README.md`, `.env` fayllarini yarating (`touch`).
3. `ls -la` bilan yashirin fayllarni ham ko'ring.
4. `README.md` ga `echo "# Loyiha" > README.md` bilan yozing va `cat` bilan o'qing.

## 🟡 O'rta (+10 XP): Qidiruv va pipe
5. `nano` bilan `src/app.py` ga 3 qator kod yozing va saqlang.
6. Botingiz papkasida: `grep -rn "async def" .` — nechta handler bor?
7. `find . -name "*.py" | wc -l` — nechta Python fayl?
8. `history | tail -n 10 > oxirgi_buyruqlar.txt`

## 🔴 Qiyin (+20 XP): Ruxsatlar
9. `salom.sh` yarating: `#!/bin/bash` va `echo "Salom, $(whoami)! Bugun $(date +%d.%m.%Y)"`. Ishga tushiring: `./salom.sh`. "Permission denied" chiqdimi? `chmod +x` bilan tuzating.
10. `ls -l` natijasidagi `-rw-r--r--` ni o'qing: kim nima qila oladi? `chmod 600 .env` qiling. Nega `.env` uchun aynan 600?
