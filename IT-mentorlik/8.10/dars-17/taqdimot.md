# 17-dars slaydlari: CSS Grid

## 1-slayd
🥕 **Grid — qator VA ustun**

## 2-slayd — Flex va Grid
Flex ➡️ bir o'lcham (qator YOKI ustun)
Grid ⬛ ikki o'lcham (jadvalga o'xshash)

## 3-slayd — Birinchi grid
```css
.galereya {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;   /* 3 ta teng ustun */
  gap: 20px;
}
```
`fr` = bo'sh joyning bir ulushi (fraction)

## 4-slayd — repeat
`repeat(4, 1fr)` = `1fr 1fr 1fr 1fr`
`200px 1fr` = chap ustun 200px, qolgani o'ngga

## 5-slayd — Cho'zish
```css
.katta { grid-column: span 2; }    /* 2 ustunni egallaydi */
.baland { grid-row: span 2; }      /* 2 qatorni egallaydi */
```

## 6-slayd — 🪄 Sehrli qator
```css
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```
Ekran kattaligiga qarab ustunlar soni avtomatik o'zgaradi. **Media query'siz!**

## 7-slayd — Sahifa maketi
```css
body {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 250px 1fr;
}
header { grid-area: header; }
```
