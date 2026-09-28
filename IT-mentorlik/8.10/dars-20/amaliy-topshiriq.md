# 20-dars amaliy topshiriq: mini-saytni telefonga moslash

## 🟢 Oson (+5 XP)
1. Barcha sahifalarda `viewport` meta tegi borligini tekshiring.
2. Barcha rasmlar: `max-width: 100%; height: auto;`
3. DevTools'da iPhone SE rejimida skrinshot oling (oldin).

## 🟡 O'rta (+10 XP)
4. Galereya: telefonda 1, planshetda 2, kompyuterda 3 ustun (mobile-first).
5. Header: telefonda logo va menyu ustma-ust (`flex-direction: column`), kompyuterda bir qatorda.
6. Telefonda shrift o'lchamlari biroz kichikroq bo'lsin.
7. Skrinshot oling (keyin). Oldin/keyin taqqoslang!

## 🔴 Qiyin (+20 XP)
8. Telefonda menyu yashirilsin va "☰" belgisi chiqsin. Ochish uchun CSS "checkbox hiylasi":
```html
<input type="checkbox" id="menu-toggle" hidden>
<label for="menu-toggle">☰</label>
<nav class="menu">...</nav>
```
```css
.menu { display: none; }
#menu-toggle:checked ~ .menu { display: block; }
@media (min-width: 768px) { .menu { display: flex; } label[for="menu-toggle"] { display: none; } }
```
