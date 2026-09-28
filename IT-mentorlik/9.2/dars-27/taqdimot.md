# 27-dars slaydlari: Linux 2 🐧⚙️

## 1-slayd
**Serverda nima ishlayapti? Qanday boshqaramiz?**

## 2-slayd — Jarayonlar
`ps aux | grep python` — python jarayonlari · `top` / `htop` — jonli monitor
`kill 1234` — to'xtatish (PID bo'yicha) · `kill -9 1234` — majburan
`python bot.py &` — fonda ishga tushirish · `Ctrl+C` to'xtatish · `Ctrl+Z` pauza

## 3-slayd — Paketlar (Ubuntu/Debian)
```bash
sudo apt update              # paketlar ro'yxatini yangilash
sudo apt install htop tree   # o'rnatish
sudo apt remove tree         # o'chirish
```

## 4-slayd — Muhit o'zgaruvchilari
```bash
echo $HOME $USER $PATH
export BOT_TOKEN="123:abc"   # faqat shu sessiya uchun
env | grep BOT
```

## 5-slayd — Tarmoq
`curl https://api.github.com` — HTTP so'rov · `ping google.com` · `ss -tulpn` — qaysi portlar ochiq · `ip a` — IP-manzil

## 6-slayd — Bash skript
```bash
#!/bin/bash
NOM=${1:-"mehmon"}          # 1-argument yoki "mehmon"
if [ -d "$HOME/loyiha" ]; then
  echo "Salom, $NOM! Loyiha papkasi bor"
fi
for f in *.py; do
  echo "Python fayl: $f"
done
```

## 7-slayd — OverTheWire Bandit 🏴‍☠️
Haqiqiy server · SSH orqali ulanish · har bir darajada keyingi parolni topish
`ssh banditN@bandit.labs.overthewire.org -p 2220`
