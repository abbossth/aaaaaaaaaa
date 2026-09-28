# 27-dars amaliy topshiriq

## 🟢 Oson (+10 XP)
1. Botingizni fonda ishga tushiring (`python bot.py &`), `ps aux | grep bot` bilan PID'ni toping, `kill` bilan to'xtating.
2. `curl -s https://api.github.com/users/<username> | head -20` — terminalda API!

## 🔴 Qiyin (+20 XP): backup skripti
`kod/backup.sh` ni o'rganing va o'zingiz yozing (yoki moslang):
- Argument sifatida papka qabul qilsin
- `tar.gz` arxiv yaratsin (nomida sana-vaqt)
- `.venv`, `__pycache__`, `.env` ni arxivga qo'shmasin (nega `.env`?)
- Faqat oxirgi 5 ta backup'ni saqlasin
- Papka topilmasa, xato bilan chiqsin (`exit 1`)

Bot loyihangizni backup qiling: `./backup.sh ~/telegram-bot`
