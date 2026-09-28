# 24-dars slaydlari: Saytingiz — butun dunyoga! 🌍

## 1-slayd
**Bugun saytingiz internetda bo'ladi!**

## 2-slayd — Git = o'yindagi "save" 💾
Har bir **commit** — saqlangan holat. Xato qilsangiz — oldingi holatga qaytasiz.
**Git** — dastur (kompyuteringizda) · **GitHub** — bulutdagi "omborxona" (sayt)

## 3-slayd — 3 qadam
✏️ Fayllarni o'zgartirasiz → ➕ **add** (tayyorlash) → 💾 **commit** (saqlash + izoh) → ☁️ **push** (GitHub'ga yuborish)

## 4-slayd — VS Code orqali (eng oson)
1. Chap panel: **Source Control** (Ctrl+Shift+G)
2. "Initialize Repository"
3. Izoh yozing: "Birinchi versiya" → ✓ **Commit**
4. "Publish to GitHub" → public → tayyor!

## 5-slayd — Terminal orqali (dasturchilar uslubi)
```bash
git init
git add .
git commit -m "Birinchi versiya"
git remote add origin https://github.com/aziz/landing.git
git push -u origin main
```

## 6-slayd — Deploy 🚀
**GitHub Pages:** repo → Settings → Pages → Branch: main → Save → 1–2 daqiqa → `aziz.github.io/landing`
**Netlify:** app.netlify.com/drop → papkani sudrab tashlang → tayyor!

## 7-slayd — SEO: Google sizni topsin
`<title>` · `<meta name="description">` · bitta `h1` · semantik teglar · `alt` · telefonga moslik

## 8-slayd — Telegram'da chiroyli preview
```html
<meta property="og:title" content="Aziz — Mening saytim">
<meta property="og:description" content="8.10 o'quvchisining birinchi sayti">
<meta property="og:image" content="https://.../rasm.jpg">
```
