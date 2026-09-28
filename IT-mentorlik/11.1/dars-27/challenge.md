# 27-dars challenge: "Server detektivi" 🕵️

**Vaqt:** 15 daqiqa | **Format:** juftlik | **Muhit:** Linux terminal

Faqat buyruqlar bilan javob toping (buyruqni ham yozing!):

| № | Savol | Maslahat |
|---|---|---|
| 1 | Server qancha vaqtdan beri ishlayapti? | `uptime` |
| 2 | Qancha RAM bor va qanchasi bo'sh? | `free -h` |
| 3 | Disk qancha to'lgan? | `df -h` |
| 4 | Qaysi portlar tinglanmoqda? 3000-portni kim egallagan? | `ss -tulpn` |
| 5 | Eng ko'p CPU ishlatayotgan 3 ta jarayon? | `ps aux --sort=-%cpu \| head -4` |
| 6 | Tizimda qaysi foydalanuvchilar bor (login qila oladiganlari)? | `grep -v nologin /etc/passwd` |
| 7 | `mvp-api` servisi oxirgi marta qachon qayta ishga tushgan? | `systemctl status mvp-api` |
| 8 | Oxirgi 5 ta tizim log yozuvi? | `journalctl -n 5` |

**XP:** 8/8 → 🥇 +20 · 🥈 +10 · 🥉 +5
