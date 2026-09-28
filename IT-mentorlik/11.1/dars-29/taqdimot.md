# 29-dars slaydlari: Nginx 🟩

## 1-slayd
**Nginx — mehmonxona resepsiyasi 🏨**

## 2-slayd — Reverse proxy
```
Brauzer ──▶ Nginx :80/443 ──┬── /          ──▶ React statik fayllar (/var/www/mvp)
                            └── /api/...   ──▶ Express :3000 (faqat ichkaridan!)
```
✅ Bitta domen, bitta port · ✅ HTTPS bir joyda · ✅ Node porti yopiq · ✅ Kesh, siqish, rate limit

## 3-slayd — Tuzilma
```
/etc/nginx/
├── nginx.conf                 ← asosiy
├── sites-available/mvp        ← sizning konfiguratsiyangiz
└── sites-enabled/mvp → ../sites-available/mvp   (symlink)
/var/log/nginx/access.log, error.log
```

## 4-slayd — Konfiguratsiya
```nginx
server {
    listen 80;
    server_name _;

    root /var/www/mvp;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;   # React SPA
    }

    location /api/ {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 5-slayd — Diagnostika 🩺
```bash
sudo nginx -t                    # sintaksisni tekshirish (DOIM!)
sudo systemctl reload nginx
curl -I http://localhost/        # sarlavhalar
sudo tail -f /var/log/nginx/error.log
```

## 6-slayd — Tipik xatolar
**502 Bad Gateway** → Express ishlamayapti yoki port noto'g'ri
**404** → `root` yo'li noto'g'ri yoki SPA uchun `try_files` yo'q
**403** → fayllarga ruxsat yo'q (`chmod`/`chown`)
