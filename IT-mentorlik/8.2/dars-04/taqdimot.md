# 4-dars slaydlari: Responsiv dizayn

## 1-slayd
📱💻🖥 **Bitta sayt — hamma ekranlar uchun**

## 2-slayd — Nega?
Veb-trafikning **60%+** qismi mobil qurilmalardan keladi.
Google mobilga moslashmagan saytlarni qidiruvda pastga tushiradi.

## 3-slayd — 1-qadam: viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Busiz telefon sahifani "kichraytirib" ko'rsatadi

## 4-slayd — Nisbiy birliklar
`%` ota elementga nisbatan · `rem` asosiy shrift o'lchamiga nisbatan (1rem = 16px)
`vw`/`vh` ekran kengligi/balandligining 1% i · `em` ota element shriftiga nisbatan

## 5-slayd — Media query
```css
/* Mobile-first: avval telefon uchun */
.cards { display: grid; grid-template-columns: 1fr; }

@media (min-width: 768px) {   /* planshet */
  .cards { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1200px) {  /* kompyuter */
  .cards { grid-template-columns: repeat(3, 1fr); }
}
```

## 6-slayd — Breakpoint'lar
📱 < 576px · 📱 576–767 · 📲 768–991 · 💻 992–1199 · 🖥 1200+

## 7-slayd — Sehrli qator ✨
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```
Media query'siz ham avtomatik moslashadi!
