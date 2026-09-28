# 29-dars tezkor test

1. Reverse proxy nima? — Mijoz so'rovlarini qabul qilib, ichki servislarga yo'naltiruvchi server
2. `/api` ni Express'ga yo'naltiruvchi direktiva? — `proxy_pass http://127.0.0.1:3000;`
3. Konfiguratsiyani tekshirish? — `sudo nginx -t`
4. 502 Bad Gateway odatda nimani bildiradi? — Nginx orqadagi servisga ulana olmadi (servis ishlamayapti yoki port noto'g'ri)
5. React SPA uchun qaysi qator kerak? — `try_files $uri $uri/ /index.html;`
6. Nginx xato loglari qayerda? — `/var/log/nginx/error.log`
