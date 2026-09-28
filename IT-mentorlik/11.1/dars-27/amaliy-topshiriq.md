# 27-dars amaliy topshiriq: Node API → systemd servisi

Muhit: WSL (Ubuntu) yoki killercoda.com (Ubuntu playground). Cheat-sheet: `kod/linux-cheatsheet.md`

## 🟢 Oson (+5 XP)
1. `sudo apt update && sudo apt install -y nodejs npm tree htop`
2. `tree /etc -L 1 | head -30` — qanday sozlamalar bor?
3. `ls -l /etc/passwd /etc/shadow` — nega ruxsatlari farq qiladi?

## 🟡 O'rta (+10 XP)
4. `deploy` foydalanuvchisini yarating. `/opt/mvp` papkasini yaratib, egasini `deploy` qiling (`chown -R`).
5. 25-darsdagi `mvp-skelet/server` ni `/opt/mvp/server` ga nusxalang (`git clone` yoki `cp -r`), `npm install`.
6. `.env` fayli yarating va `chmod 600` bering. `ls -l` bilan tekshiring.

## 🔴 Qiyin (+20 XP)
7. `kod/mvp-api.service` ni `/etc/systemd/system/` ga qo'ying.
8. `sudo systemctl daemon-reload && sudo systemctl enable --now mvp-api`
9. `curl localhost:3000/api/health` — ishlayaptimi?
10. Jarayonni "o'ldiring": `sudo kill -9 $(pgrep -f "node src/index.js")`. 3 soniyadan keyin `systemctl status mvp-api` — **qayta turdimi?** 🧟
11. `journalctl -u mvp-api -n 20` — loglarni o'qing.
