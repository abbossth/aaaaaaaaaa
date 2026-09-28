# 29-dars amaliy topshiriq: MVP → Nginx ortida

Muhit: 27-darsdagi server/WSL/killercoda (Express systemd servisi ishlab turibdi).

## 🟢 Oson (+10 XP)
1. `sudo apt install -y nginx` → brauzerda (yoki `curl localhost`) "Welcome to nginx!" sahifasi.
2. `ls /etc/nginx/sites-enabled/`, `cat /etc/nginx/sites-available/default` — tuzilishini o'qing.

## 🟡 O'rta (+10 XP): reverse proxy
3. `kod/mvp.nginx.conf` ni `/etc/nginx/sites-available/mvp` ga qo'ying, symlink yarating, `default` ni o'chiring.
4. `sudo nginx -t && sudo systemctl reload nginx`
5. `curl http://localhost/api/health` → Express javobi Nginx orqali keldimi? 🎉
6. `sudo tail -n 5 /var/log/nginx/access.log` — so'rovingiz ko'rinyaptimi?

## 🔴 Qiyin (+20 XP): React + API bitta domenda
7. `cd web && npm run build` → `sudo mkdir -p /var/www/mvp && sudo cp -r dist/* /var/www/mvp/`
8. Brauzerda `http://<server-ip>/` — React ilova ochiladi va `/api` orqali ma'lumot oladi (endi Vite proxy'siz!).
9. `ufw` da 3000-port **yopiq**ligini tekshiring: tashqaridan faqat 80 orqali kirish mumkin.
