# 13-dars slaydlari: CSS — sahifaga kiyim

## 1-slayd
🎨 **HTML = skelet · CSS = kiyim**

## 2-slayd — CSS sintaksisi
```css
h1 {
  color: blue;
  font-size: 40px;
}
```
`h1` selektor · `color` xossa · `blue` qiymat · `;` har bir qator oxirida

## 3-slayd — 3 ulash usuli
1️⃣ Inline: `<h1 style="color: red;">` ❌ (tartibsiz)
2️⃣ Internal: `<style>` teg ichida `<head>` da ⚠️ (bitta sahifa uchun)
3️⃣ External: `<link rel="stylesheet" href="style.css">` ✅ (hamma sahifa uchun bitta fayl)

## 4-slayd — Selektorlar
`p` — barcha paragraflar
`.karta` — `class="karta"` bo'lgan barcha elementlar
`#logo` — `id="logo"` bo'lgan bitta element
`h1, h2` — ikkalasiga
`nav a` — nav ichidagi havolalar

## 5-slayd — Ranglar
`red` nomi · `#ff0000` HEX · `rgb(255, 0, 0)` RGB · `rgba(255, 0, 0, 0.5)` shaffof
🎨 Palitra tanlash: **coolors.co**

## 6-slayd — Matn xossalari
`color` rang · `font-family` shrift · `font-size` o'lcham · `font-weight: bold` qalinlik
`text-align: center` tekislash · `line-height: 1.6` qatorlar oralig'i · `text-decoration: none`

## 7-slayd — Google Fonts
fonts.google.com → shrift tanlash → `<link>` ni nusxalash → `<head>` ga
```css
body { font-family: "Poppins", sans-serif; }
```
