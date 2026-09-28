# 27-dars slaydlari: Linux server asoslari 🐧

## 1-slayd
**Noutbuk yopildi → startap o'ldi?** Yo'q, agar u serverda bo'lsa!

## 2-slayd — Muhim papkalar
`/etc` sozlamalar (nginx, ssh) · `/var/log` loglar · `/usr/bin` dasturlar
`/home/user` foydalanuvchi · `/opt` qo'shimcha dasturlar · `/tmp` vaqtinchalik

## 3-slayd — Ruxsatlar
```
-rwxr-x---  app  deploy  server.sh
 egasi|guruh|boshqalar
```
`chmod 750 server.sh` (7=rwx 5=r-x 0=---) · `chmod u+x,o-r f`
`chown app:deploy server.sh`
**Least privilege:** har kimga faqat kerakli minimal huquq

## 4-slayd — Foydalanuvchilar
```bash
sudo adduser deploy
sudo usermod -aG sudo deploy   # sudo guruhiga qo'shish
su - deploy                    # foydalanuvchini almashtirish
```
Ilovani **root** sifatida ishga tushirmang!

## 5-slayd — Paketlar
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y nginx curl git
```

## 6-slayd — systemd: servislar menejeri
```bash
sudo systemctl status nginx
sudo systemctl restart nginx
sudo systemctl enable nginx      # server yoqilganda avtomatik ishga tushadi
journalctl -u nginx -f           # servis loglari (jonli)
```

## 7-slayd — O'z servisimiz
```ini
# /etc/systemd/system/mvp-api.service
[Unit]
Description=Startap MVP API
After=network.target

[Service]
User=deploy
WorkingDirectory=/opt/mvp/server
ExecStart=/usr/bin/node src/index.js
Restart=always
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```
