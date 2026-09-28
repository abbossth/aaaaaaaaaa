# 7-dars slaydlari: Git, GitHub va deploy

## 1-slayd
🌍 **Bugun saytingiz butun dunyoga ochiladi!**

## 2-slayd — Git = o'yindagi "save point" 💾
Har bir commit — saqlangan holat. Xato qilsangiz, oldingi holatga qaytasiz.
**GitHub** — save'larni bulutda saqlaydigan va jamoa bilan ulashadigan joy.

## 3-slayd — Birinchi sozlash (bir marta)
```bash
git config --global user.name "Aziz Karimov"
git config --global user.email "aziz@example.com"
```

## 4-slayd — Asosiy sikl
```bash
git init                          # repo yaratish
git add .                         # o'zgarishlarni tayyorlash
git commit -m "Landing page"      # saqlash
git remote add origin https://github.com/aziz/landing.git
git branch -M main
git push -u origin main           # GitHub'ga yuborish
```
Keyingi safar: `git add .` → `git commit -m "..."` → `git push`

## 5-slayd — Deploy = saytni internetga joylash
🟢 **GitHub Pages:** Settings → Pages → Branch: main → Save → `aziz.github.io/landing`
🟢 **Netlify:** app.netlify.com → "Add new site" → GitHub'dan import → `aziz-landing.netlify.app`

## 6-slayd — SEO: Google sizni topishi uchun
```html
<title>Aziz — Veb-dasturchi portfoliosi</title>
<meta name="description" content="8-sinf o'quvchisi Azizning loyihalari">
```
+ semantik teglar, `alt`, bitta `h1`, tez yuklanish, mobilga moslik

## 7-slayd — Open Graph: Telegram'dagi chiroyli preview
```html
<meta property="og:title" content="CodeKids — IT to'garak">
<meta property="og:description" content="Kelajak kasbini bugun o'rgan!">
<meta property="og:image" content="https://.../preview.jpg">
```
