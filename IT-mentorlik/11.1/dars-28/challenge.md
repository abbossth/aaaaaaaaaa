# 28-dars challenge: "Serverni mustahkamla" 🛡

**Vaqt:** 18 daqiqa | **Format:** jamoalar

Mentor har bir jamoaga **ataylab zaif** sozlangan o'quv serveri (yoki killercoda muhiti) beradi. Unda 6 ta xavfsizlik muammosi bor. Ularni toping va tuzating:

| № | Muammo (yashirin) | Qanday topiladi |
|---|---|---|
| 1 | Parol bilan SSH ruxsat etilgan | `grep PasswordAuthentication /etc/ssh/sshd_config` |
| 2 | Root login ruxsat etilgan | `grep PermitRootLogin ...` |
| 3 | Firewall o'chiq | `sudo ufw status` |
| 4 | `.env` fayli hammaga o'qish uchun ochiq (644) | `ls -l /opt/mvp/server/.env` |
| 5 | Ilova root sifatida ishlayapti | `ps aux \| grep node` |
| 6 | Keraksiz port ochiq (masalan, 5432 hammaga) | `ss -tulpn` |

**XP:** har bir tuzatilgan muammo +5 · birinchi 6/6 → +20
**Diqqat:** SSH sozlamasini o'zgartirishdan oldin **ikkinchi terminalda** ulanib turing — xato qilsangiz, serverdan "qulflanib" qolmaysiz!
